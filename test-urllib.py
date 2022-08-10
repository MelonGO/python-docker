from urllib import request, parse, error
import urllib
import ssl
import socket

from urllib.request import urlopen
from urllib.request import build_opener
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler
from urllib.request import ProxyHandler
import http.cookiejar
from urllib.error import URLError

from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote

from urllib.robotparser import RobotFileParser

ssl._create_default_https_context = ssl._create_unverified_context

# ----------------urllib.request.urlopen-------------------
# response = urllib.request.urlopen('https://www.baidu.com')  
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
#---------------------------------------------------


# -------------------data-------------------
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')  
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)  
# print(response.read().decode('utf-8'))
#---------------------------------------------------


# -------------------timeout-------------------
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)  
# print(response.read())
#---------------------------------------------------
# try:  
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)  
# except urllib.error.URLError as e:  
#     if isinstance(e.reason, socket.timeout):  
#         print('TIME OUT')
#---------------------------------------------------
# urllib.request.Request
# request = urllib.request.Request('https://python.org')  
# response = urllib.request.urlopen(request)  
# print(response.read().decode('utf-8'))
#---------------------------------------------------


#-------class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)--------
# url = 'http://httpbin.org/post'  
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',  
#     'Host': 'httpbin.org'  
# }  
# dict = {'name': 'Germey'}  
# data = bytes(parse.urlencode(dict), encoding='utf8')  
# req = request.Request(url=url, data=data, headers=headers, method='POST')  
# response = request.urlopen(req)  
# print(response.read().decode('utf-8'))
#---------------------------------------------------


# -------------------add_header-------------------
# req = request.Request(url=url, data=data, method='POST')  
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
#---------------------------------------------------


#-------------------Handler_Auth_验证-------------------
# username = 'admin'  
# password = 'admin'  
# url = 'https://ssr3.scrape.center/'  

# p = HTTPPasswordMgrWithDefaultRealm()  
# p.add_password(None, url, username, password)  
# auth_handler = HTTPBasicAuthHandler(p)  
# opener = build_opener(auth_handler)  

# try:  
#     result = opener.open(url)  
#     html = result.read().decode('utf-8')  
#     print(html)  
# except URLError as e:  
#     print(e.reason)
#---------------------------------------------------


#-------------------Handler_Proxy_代理-------------------
# proxy_handler = ProxyHandler({
#     'http': 'http://141.164.37.2:443',
#     'https': 'https://141.164.37.2:443'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
#---------------------------------------------------


#-------------------Handler_Cookie-------------------
# cookie = http.cookiejar.CookieJar()  
# handler = urllib.request.HTTPCookieProcessor(cookie)  
# opener = urllib.request.build_opener(handler)  
# response = opener.open('http://www.baidu.com')  
# for item in cookie:  
#     print(item.name+"="+item.value)
#---------------------------------------------------
# filename = 'cookies.txt'  
# # cookie = http.cookiejar.MozillaCookieJar(filename)  
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)  
# opener = urllib.request.build_opener(handler)  
# response = opener.open('https://www.pornhub.com')  
# cookie.save(ignore_discard=True, ignore_expires=True)
#---------------------------------------------------
# cookie = http.cookiejar.LWPCookieJar()  
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)  
# handler = urllib.request.HTTPCookieProcessor(cookie)  
# opener = urllib.request.build_opener(handler)  
# response = opener.open('http://www.pornhub.com')  
# print(response.read().decode('utf-8'))
#---------------------------------------------------


#----------------Exception Catch----------------
# try:  
#     response = request.urlopen('https://cuiqingcai.com/404')  
# except error.URLError as e:  
#     print(e.reason)
#---------------------------------------------------
# try:  
#     response = request.urlopen('https://cuiqingcai.com/404')  
# except error.HTTPError as e:  
#     print(e.reason, e.code, e.headers, sep='\n')  
# except error.URLError as e:  
#     print(e.reason)  
# else:  
#     print('Request Successfully')
#---------------------------------------------------
# filename = 'cookies.txt'  
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)  
# opener = urllib.request.build_opener(handler)
# try:
#      response = opener.open('https://www.91porn.com')  
# except error.HTTPError as e:  
#     print(e.reason, e.code, e.headers, sep='\n')  
# except error.URLError as e:  
#     print(e.reason)  
# else:  
#     cookie.save(ignore_discard=True, ignore_expires=True)
#     print('Request Successfully')
#---------------------------------------------------
# try:  
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)  
# except urllib.error.URLError as e:  
#     print(type(e.reason))  
#     if isinstance(e.reason, socket.timeout):  
#         print('TIME OUT')
#---------------------------------------------------


#-----------------urlparse, urlunparse, urlsplit, urlunsplit-----------------
#urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')  
# print(type(result), result)
# print(result.scheme, result[0], result.netloc, result[1], sep='\n')
#---------------------------------------------------
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']  
# print(urlunparse(data))
#---------------------------------------------------
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')  
# print(result)
#---------------------------------------------------
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']  
# print(urlunsplit(data))
#---------------------------------------------------


#------------------------urljoin--------------------------
# print(urljoin('http://www.baidu.com', 'FAQ.html'))  
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))  
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))  
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))  
# print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))  
# print(urljoin('http://www.baidu.com', '?category=2#comment'))  
# print(urljoin('www.baidu.com', '?category=2#comment'))  
# print(urljoin('www.baidu.com#comment', '?category=2'))
#---------------------------------------------------


#------------------------urlencode, parse_qs, parse_qsl--------------------------
# params = {  
#     'name': 'germey',  
#     'age': 22  
# }  
# base_url = 'http://www.baidu.com?'  
# url = base_url + urlencode(params)  
# print(url)
#---------------------------------------------------
# query = 'name=germey&age=22'  
# print(parse_qs(query))
#---------------------------------------------------
# query = 'name=germey&age=22'  
# print(parse_qsl(query))
#---------------------------------------------------


#------------------------quote, unquote--------------------------
# keyword = ' 壁纸 '  
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)  
# print(url)
#---------------------------------------------------
# url = 'https://www.baidu.com/s?wd=%20%E5%A3%81%E7%BA%B8%20'  
# print(unquote(url))
#---------------------------------------------------


#------------------------RobotFileParser--------------------------
# rp = RobotFileParser()
# rp.set_url('https://www.baidu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('Googlebot', 'https://www.baidu.com/'))
# print(rp.can_fetch('Baiduspider', "https://www.baidu.com/homepage"))
#---------------------------------------------------
# rp = RobotFileParser()
# rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/'))
# print(rp.can_fetch('Googlebot', "https://www.baidu.com/homepage"))
#---------------------------------------------------






