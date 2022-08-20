import requests
import logging
import re
import random
import time
import json
import os
import tmp, tmp2
import myProxy, myHeader

# from os import makedirs
# from os.path import exists

import pymongo

import multiprocessing


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# RESULTS_DIR = 'results'
# exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'wedding'
MONGO_COLLECTION_NAME = 'shops'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['wedding']
collection = db['shops']

BASE_URL = 'https://www.dianping.com/guangzhou/ch55/g163p'

def scrape_page(url, headers):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=headers, proxies=myProxy.getCurrent())
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
        return None
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = ''
    if page == 1:
        index_url = BASE_URL + str(page)
    else:
        index_url = BASE_URL + str(page) + '?aid=f3314c1a20350bb68db5235ecb588b87'
    return scrape_page(index_url, myHeader.getHeader(1))


def parse_index(html):
    pattern = re.compile('<a\s?class="shopname".*?href="(.*?)"\s+', re.S)
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = 'https://www.dianping.com' + item
        yield detail_url


def scrape_detail(url):
    tmp_url  = url + '/review_all'
    referer = url
    return scrape_page(tmp_url, myHeader.getHeader(url))

def parse_detail(html):
    pattern_1 = re.compile('<span\s?class="PageMore">.*?review_all/p(\d+)"\s?data-pg', re.S)
    pattern_2 = re.compile('<span class="PageSel">.*PageLink"\s?title="(\d+)"', re.S)
    total_page = ''

    if re.search(pattern_1, html):
        total_page = re.search(pattern_1, html).group(1).strip()
    else:
        total_page = re.search(pattern_2, html).group(1
            ).strip() if re.search(pattern_2, html) else None

    return total_page


# def save_data(data):
#     name = data.get('name')
#     data_path = f'{RESULTS_DIR}/{name}.json'
#     json.dump(data, open(data_path, 'w', encoding='utf-8'), 
#         ensure_ascii=False, indent=2)
def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)

def find_data(name):
    data = collection.find_one({'name':name})
    if data:
        return data
    else:
        return None

def main(page):
    index_html = scrape_index(page)
    time.sleep(3)
    if index_html != None:
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            pattern = re.compile('<title>验证中心</title>', re.S)
            if re.search(pattern, detail_html):
                print('---Need Verification---')
                print('detail_html is None')
                time.sleep(100)
            time.sleep(5)
            if detail_html != None:
                total_page = parse_detail(detail_html)
                if total_page == None:
                    total_page = '1'

                pattern = re.compile('<h1 class="shop-name">(.*?)</h1>', re.S)
                shopName = re.search(pattern, detail_html).group(1
                    ).strip() if re.search(pattern, detail_html) else None

                pattern = re.compile('<span class="reviews">(\d+)条评价</span>', re.S)
                total = re.search(pattern, detail_html).group(1
                    ).strip() if re.search(pattern, detail_html) else None

                pattern = re.compile('<span class="price">人均：(\d+)元</span>', re.S)
                price = re.search(pattern, detail_html).group(1
                    ).strip() if re.search(pattern, detail_html) else None

                pattern = re.compile('<span class="score">\s+<span class="item">(.*?)</span>\s+<span class="item">(.*?)</span>\s+<span class="item">(.*?)</span>\s+</span>', re.S)
                score = re.search(pattern, detail_html) if re.search(pattern, detail_html) else None
                if score != None:
                    scores = [score.group(1), score.group(2), score.group(3)]
                else:
                    pattern = re.compile('<div class="star_score.*?">(.*?)</div>', re.S)
                    score = re.search(pattern, detail_html) if re.search(pattern, detail_html) else None
                    if score != None:
                        score = [score.group(1)]
                    else:
                        score = ['0']
                
                data = find_data(shopName)
                if data == None:
                    data = {
                        'name':shopName,
                        'total':total,
                        'price':price,
                        'score':scores,
                        'comments':{},
                    }
                    save_data(data)

                commentsDic = {}
                print('total_page is ' + total_page)
                for each_page in range(1, int(total_page)+1):
                    data = find_data(shopName)
                    if str(each_page) in data['comments'].keys():
                        continue
                    else:
                        comments = tmp2.main(detail_url, each_page)
                        if comments != None:
                            data['comments'][str(each_page)] = comments
                            save_data(data)
                            time.sleep(random.randint(8, 10))
                        else:
                            print('---Need Verification---')
                            time.sleep(100)


if __name__ == '__main__':
    # pool = multiprocessing.Pool()
    # pages = [26, 27]
    # pool.map(main, pages)
    # pool.close()
    main(28)
