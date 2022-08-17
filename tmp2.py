import requests
import logging
import re
import sys
import random
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# BASE_URL = 'https://www.dianping.com/shop/iVgtZC1q4rwv35JV'
headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',}
Cookie = 'fspop=test; _hc.v=8ba6219a-4376-1c22-0956-8ca1e8947e9c.1660573650; aburl=1; cy=4; cye=guangzhou; wed_user_path=163|0; ctu=c24d9f2d8f056fe3b1bd3d4b748d21ccf9fd8b3c724cd87209f5c9cc129eaf29; _lxsdk_cuid=182a80705ae13-0e151959ae61be-1b525635-384000-182a80705b3c8; _lxsdk=182a80705ae13-0e151959ae61be-1b525635-384000-182a80705b3c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1660676410; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1660676413; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1660676413; wedchatguest=g-116216354276421970; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1660676429; WEBDFPID=277x1u58771154791u39270x014v0zyy817z1922521979588uzv9131-1660762837205-1660676436466QMAICEU75613c134b6a252faa6802015be905511823; dplet=0d775ab358b90eabae51688bca9e1d09; dper=52d133157ed9cd5652efb9aa386c2a43f80417a7eb139a7915ae5e9552059fb2f3c2a4078b11aabf4965c3341412ba6b85b828e4966e219282167a26989b20fde81972d23a83aaa18aeff57ef17d131bcc1724c2b5c0b704491dc379f5e305f2; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6981982693; _lxsdk_s=182a80705b9-fa4-126-e3f%7C%7C196'


def random_ip():
    a=random.randint(1, 255)
    b=random.randint(1, 255)
    c=random.randint(1, 255)
    d=random.randint(1, 255)
    return (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))

def scrape_page(url, base_url, cookie, proxies):
    logging.info('scraping %s...', url)
    try:
        headers={'Accept-Language':'zh-CN,zh;q=0.9',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
                 'X-Forwarded-For': random_ip(),
                 'referer': base_url,
                 'Content-Type': 'multipart/form-data; session_language=cn_CN',
                 'Connection': 'keep-alive',
                 'Upgrade-Insecure-Requests': '1',
                 'Cookie': cookie,
                 }
        response = requests.get(url, headers=headers, proxies=proxies)
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
        print('BLOCK')
        return 'BLOCK'
    pattern = re.compile('href="//(s3plus\.meituan\.net.*?css)">', re.S)
    css_url = re.search(pattern, html).group(1
            ).strip() if re.search(pattern, html) else None
    css_url = 'https://' + css_url
    return css_url

def scrape_css(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=headers1)
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
    svg_response = requests.get(url=svg_url,headers=headers1)
    # with open("./" + "某众点评.svg",mode='w',encoding='UTF-8') as f:
    #     f.write(svg_response.text)

    '''
    .rizms{background:-406.0px -1292.0px;}
    '''
    pattern = re.compile('.'+key_letter+'(\w+){background:-(\d+)\.0px -(\d+)\.0px;', re.S)
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
        tmp = item[2] + 23
        index = item[1] / 14
        word = lines[path[tmp]][int(index): int(index)+1]
        resDic[item[0]] = word
    # print(resDic)
    
    return resDic


def main(base_url, page, cookie, proxies):
    url = ''
    if page == 1:
        url = base_url
    else:
        url = base_url + '/p' + str(page)
    content = scrape_page(url, base_url, cookie, proxies)
    if content == None:
        return None
    css_url = parse_content(content)
    css_content = scrape_css(css_url)
    resDic = parse_css(css_content)

    result = []

    comment_list = re.findall('<div class="review-words">\s+(.*?)\s+<div>', content, re.S)
    for i in comment_list:
        key_list = re.findall('<svgmtsi class="(\w+)"></svgmtsi>', i, re.S)
        for n in key_list:
            #把svgmtsi标签替换成正确汉字
            i = i.replace('<svgmtsi class="{}"></svgmtsi>'.format(n), resDic[n])
            #替换掉文本中的img标签和一些其它符号
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
        result.append(i)

    # print(result)
    return result


if __name__ == '__main__':
    proxies = {
            'http': 'http://141.164.37.2:3128',
            'https': 'http://141.164.37.2:3128',
            }
    main('https://www.dianping.com/shop/iRuCAwsPTOfDXszM/review_all', 2, Cookie, proxies)






