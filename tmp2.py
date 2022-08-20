import requests
import logging
import re
import sys
import random
import time
import os
import myHeader, myProxy

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',}

def scrape_page(url, referer):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=myHeader.getHeader(referer), proxies=myProxy.getCurrent())
        if response.status_code == 200:
            # with open("./" + '某众点评.html','w',encoding='UTF-8') as f:
            #     f.write(response.text)
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
        return None
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def parse_content(html):
    pattern = re.compile('<title>验证中心</title>', re.S)
    if re.search(pattern, html):
        print('验证中心')
        return None
    pattern = re.compile('href="//(s3plus\.meituan\.net.*?css)">', re.S)
    css_url = re.search(pattern, html).group(1
            ).strip() if re.search(pattern, html) else None
    if css_url == None:
        print(html)
        print('css_url is None')
        return None
    css_url = 'https://' + css_url
    return css_url

def scrape_css(url):
    # logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=headers1, proxies=myProxy.getCurrent())
        if response.status_code == 200:
            response.encoding = 'windows-1252'
            # with open("./" + r'某众点评.css','w',encoding='UTF-8') as f:
            #     f.write(response.text)
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

def parse_css(html):
    pattern = re.compile('svgmtsi\[class\^="(\w+)"].*?background-image:\s?url\((.*?)\);', re.S)
    svg_group = re.search(pattern, html) if re.search(pattern, html) else None
    #key_letter：公共前缀
    key_letter = svg_group[1]
    #注意拼接上http
    svg_url = 'http:' + svg_group[2]
    svg_response = requests.get(url=svg_url,headers=headers1, proxies=myProxy.getCurrent())
    # with open("./" + "某众点评.svg",mode='w',encoding='UTF-8') as f:
    #     f.write(svg_response.text)

    '''
    .rizms{background:-406.0px -1292.0px;}
    '''
    pattern = re.compile('\.'+key_letter+'(\w+){background:-(\d+)\.0px -(\d+)\.0px;', re.S)
    class_map = re.findall(pattern, html) if re.findall(pattern, 
        html) else []
    class_map = [(key_letter + cls_name, int(x), int(y)) for cls_name,x,y in class_map]
    # print(class_map)

    '''
    <defs><path id="1" d="M0 39 H600"/><path id="2" d="M0 70 H600"/></defs>
    <textPath xlink:href="#8" textLength="448">灶与秘苏哄晨率党镇坑拒纠刻鹅霸避浩出池育霉鹊闯截绑碑驴塌悠垃寇喉</textPath>
    '''
    pattern = re.compile('<path id="(\d+)" d="M0 (\d+) H600"/>', re.S)
    tmp = re.findall(pattern, svg_response.text) if re.findall(pattern, 
        svg_response.text) else []
    path = {}
    for item in tmp:
        path[int(item[1])] = int(item[0])
    # print(path)

    pattern = re.compile('<textPath xlink:href="#(\d+)" textLength="\d+">(.*?)</textPath>', re.S)
    items = re.findall(pattern, svg_response.text) if re.findall(pattern, 
        svg_response.text) else []
    lines = {}
    for item in items:
        lines[int(item[0])] = item[1]
    # print(lines)

    resDic = {}
    for item in class_map:
        # print(item)
        tmp = item[2] + 23
        index = item[1] / 14
        word = lines[path[tmp]][int(index): int(index)+1]
        resDic[item[0]] = word
    # print(resDic)
    
    return resDic


def main(base_url, page):
    url = ''
    if page == 1:
        url = base_url + '/review_all'
    else:
        url = base_url + '/review_all/p' + str(page)
    referer = base_url
    content = scrape_page(url, referer)
    if content == None:
        print(url + ' is None')
        return None
    css_url = parse_content(content)
    if css_url == None:
        print(url)
        return None
    css_content = scrape_css(css_url)
    resDic = parse_css(css_content)

    result = []

    comment_list = re.findall('<div class="review-words">\s+(.*?)\s+</div>', content, re.S)
    for i in comment_list:
        key_list = re.findall('<svgmtsi class="(\w+)"></svgmtsi>', i, re.S)
        for n in key_list:
            #把svgmtsi标签替换成正确汉字
            i = i.replace('<svgmtsi class="{}"></svgmtsi>'.format(n), resDic[n])
            #替换掉文本中的img标签和一些其它符号
            i = re.sub(r'<img (.*?)/>',"", i)
            i = re.sub(r'&(.*?);',"", i)
        i = re.sub(r'<img (.*?)/>',"", i)
        i = re.sub(r'&(.*?);',"", i)
        result.append(i)
    
    comment_list = re.findall('<div class="review-words Hide">\s+(.*?)\s+<div class="less-words">', content, re.S)
    for i in comment_list:
        key_list = re.findall('<svgmtsi class="(\w+)"></svgmtsi>', i, re.S)
        for n in key_list:
            #把svgmtsi标签替换成正确汉字
            i = i.replace('<svgmtsi class="{}"></svgmtsi>'.format(n), resDic[n])
            #替换掉文本中的img标签和一些其它符号
            i = re.sub(r'<img (.*?)/>',"", i)
            i = re.sub(r'&(.*?);',"", i)
        i = re.sub(r'<img (.*?)/>',"", i)
        i = re.sub(r'&(.*?);',"", i)
        result.append(i)

    # print(result)
    return result


if __name__ == '__main__':
    main('https://www.dianping.com/shop/G6NEZrYjgv8FWuD7/review_all', 1)






