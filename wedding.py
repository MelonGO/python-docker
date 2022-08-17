import requests
import logging
import re
import random
import time
import json
from urllib.parse import urljoin
import tmp, tmp2

from os import makedirs
from os.path import exists

import multiprocessing

import tmp

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

BASE_URL = 'https://www.dianping.com/guangzhou/ch55/g163p'
DETAIL_URL = 'https://www.dianping.com/'
Cookie = 'fspop=test; _hc.v=8ba6219a-4376-1c22-0956-8ca1e8947e9c.1660573650; aburl=1; cy=4; cye=guangzhou; wed_user_path=163|0; ctu=c24d9f2d8f056fe3b1bd3d4b748d21ccf9fd8b3c724cd87209f5c9cc129eaf29; _lxsdk_cuid=182a80705ae13-0e151959ae61be-1b525635-384000-182a80705b3c8; _lxsdk=182a80705ae13-0e151959ae61be-1b525635-384000-182a80705b3c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1660676410; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1660676413; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1660676413; wedchatguest=g-116216354276421970; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1660676429; WEBDFPID=277x1u58771154791u39270x014v0zyy817z1922521979588uzv9131-1660762837205-1660676436466QMAICEU75613c134b6a252faa6802015be905511823; dplet=0d775ab358b90eabae51688bca9e1d09; dper=52d133157ed9cd5652efb9aa386c2a43f80417a7eb139a7915ae5e9552059fb2f3c2a4078b11aabf4965c3341412ba6b85b828e4966e219282167a26989b20fde81972d23a83aaa18aeff57ef17d131bcc1724c2b5c0b704491dc379f5e305f2; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6981982693; _lxsdk_s=182a80705b9-fa4-126-e3f%7C%7C196'

proxy_1 = {'http': 'http://141.164.37.2:3128' ,'https': 'http://141.164.37.2:3128' }
proxy_2 = {'http': 'http://45.32.122.144:3128' ,'https': 'http://45.32.122.144:3128' }
proxy_3 = {'http': 'http://45.77.11.139:3128' ,'https': 'http://45.77.11.139:3128' }

proxy_pool = [proxy_1, proxy_2, proxy_3]

def random_ip():
    a=random.randint(1, 255)
    b=random.randint(1, 255)
    c=random.randint(1, 255)
    d=random.randint(1, 255)
    return (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))


def scrape_page(url, referer):
    logging.info('scraping %s...', url)
    try:
        headers={'Accept-Language':'zh-CN,zh;q=0.9',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
                 'X-Forwarded-For': random_ip(),
                 'referer': referer,
                 'Content-Type': 'multipart/form-data; session_language=cn_CN',
                 'Connection': 'keep-alive',
                 'Upgrade-Insecure-Requests': '1',
                 'Cookie': Cookie,

                 }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
        return None
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}{page}'
    referer = BASE_URL + str(page) + '?aid=f3314c1a20350bb68db5235ecb588b87'
    return scrape_page(index_url, referer)


def parse_index(html):
    pattern = re.compile('<a\s?class="shopname".*?href="(.*?)"\s+', re.S)
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(DETAIL_URL, item + '/review_all')
        logging.info('get detail url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    referer = url
    return scrape_page(url, referer)

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


# def scrape_review(url, page):
#     referer = url
#     url = url + '/p' + str(page)
#     return scrape_page(url, referer)

# def parse_review(html):
#     css_url = tmp.parse_content(html)
#     css_content = tmp.scrape_css(css_url)
#     svg_result = tmp.parse_css(css_content)

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

def main(page):
    index_html = scrape_index(page)
    time.sleep(3)
    if index_html != None:
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            time.sleep(4)
            if detail_html != None:
                total_page = parse_detail(detail_html)

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
                scores = [score.group(1), score.group(2), score.group(3)]

                comments_list = []

                for each_page in range(1, int(total_page)):
                    comments = tmp2.main(detail_url, each_page, Cookie, proxy_pool[0])
                    if comments != None:
                        comments_list.append(comments)
                        time.sleep(random.randint(5, 6))
                    else:
                        print('Cannot get reviews!!!')
                        time.sleep(random.randint(8, 10))

                data = {
                'name':shopName,
                'total':total,
                'price':price,
                'score':scores,
                'comments':comments_list
                }
                save_data(data)


if __name__ == '__main__':
    main(1)
