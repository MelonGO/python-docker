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
Cookie = '__mta=175553437.1660573945710.1660655114407.1660655114431.10; fspop=test; _lxsdk_cuid=182a1e70c1dc8-0d11e3dd763653-1b525635-384000-182a1e70c1dc8; _lxsdk=182a1e70c1dc8-0d11e3dd763653-1b525635-384000-182a1e70c1dc8; _hc.v=8ba6219a-4376-1c22-0956-8ca1e8947e9c.1660573650; aburl=1; cy=4; cye=guangzhou; wed_user_path=163|0; wedchatguest=g27364098273942395; dplet=d50c1b53c83b24b2253e76c78717021f; dper=52d133157ed9cd5652efb9aa386c2a43eefe060781e232058fd2e395558afb298f4298afe334277c21fae0272113327d8e0df404a5fd7123d19dbda5ecbdef2d994222b7bc282ce110dbf1d233128c41db13bec1aea6522fb4456913b3df5a74; ua=dpuser_6981982693; ctu=c24d9f2d8f056fe3b1bd3d4b748d21ccf9fd8b3c724cd87209f5c9cc129eaf29; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1660573651,1660654772; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1660573654,1660654792; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1660655108; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1660655123; _lxsdk_s=182a6bcdd0d-b1b-6a8-a85%7C%7C260'


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
    .zmto4{background:-42.0px -538.0px;
    '''
    pattern = re.compile('.'+key_letter+'(\w+){background:-(\d+)\.0px -(\d+)\.0px;', re.S)
    class_map = re.findall(pattern, html) if re.findall(pattern, 
        html) else []
    class_map = [(key_letter + cls_name, int(x), int(y)) for cls_name,x,y in class_map]
    print(class_map)

    '''
    <text x="0" y="2107">霉们求舍涨淡窗释槽宇搏划考止未补财脚以呈源吓峰枪赔晓贷警傅业址桶举仙逐贿于班受一顽标</text>
    '''
    pattern = re.compile('<text x="0" y="(\d+)">(.*?)</text>', re.S)
    items = re.findall(pattern, svg_response.text) if re.findall(pattern, 
        svg_response.text) else []
    lines = {}
    for item in items:
        lines[item[0]] = item[1]
    print(lines)

    resDic = {}
    for item in class_map:
        tmp = item[2] + 23
        index = item[1] / 14
        word = lines[str(tmp)][int(index): int(index)+1]
        resDic[item[0]] = word
    print(resDic)
    
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

    comment_list = re.findall('<div class="review-words Hide">\s+(.*?)\s+<div class="less-words">', content, re.S)
    result = []
    for i in comment_list:
        key_list = re.findall('<svgmtsi class="(\w+)"></svgmtsi>', i, re.S)
        for n in key_list:
            #把svgmtsi标签替换成正确汉字
            i = i.replace('<svgmtsi class="{}"></svgmtsi>'.format(n), resDic[n])
            #替换掉文本中的img标签和一些其它符号
            i = re.sub(r'<img (.*?)/>',"", i)
            i = re.sub(r'&(.*?);',"", i)
        result.append(i)
    print(result)
    return result


if __name__ == '__main__':
    proxies = {
            'http': 'http://158.247.233.4:3128',
            'https': 'http://158.247.233.4:3128',
            }
    main('https://www.dianping.com/shop/G5bPooXlxdqew9k4/review_all', 1, Cookie, proxies)






