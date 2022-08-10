import requests
import re

from requests.packages import urllib3
import logging

from requests.auth import HTTPBasicAuth

from requests import Request, Session

# r = requests.get('https://www.baidu.com/')  
# print(type(r))  
# print(r.status_code)  
# print(type(r.text))  
# print(r.text[:100])  
# print(r.cookies)

# r = requests.post('http://httpbin.org/post')  
# r = requests.put('http://httpbin.org/put')  
# r = requests.delete('http://httpbin.org/delete')  
# r = requests.head('http://httpbin.org/get')  
# r = requests.options('http://httpbin.org/get')

#---------------------GET---------------------------
# r = requests.get('http://httpbin.org/get')  
# print(r.text)
#---------------------------------------------------
# data = {  
#     'name': 'germey',  
#     'age': 22  
# }  
# r = requests.get("http://httpbin.org/get", params=data)  
# print(r.text)
#---------------------------------------------------
# r = requests.get("http://httpbin.org/get")  
# print(type(r.text))  
# print(r.json())  
# print(type(r.json()))
#---------------------------------------------------
# r = requests.get("https://ssr1.scrape.center")
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
#---------------------------------------------------
# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)
#---------------------------------------------------
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
#---------------------------------------------------
# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
#---------------------------------------------------
# r = requests.get('https://ssr1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
#---------------------------------------------------
# r = requests.get('https://ssr1.scrape.center/')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
#---------------------------------------------------


#---------------------POST--------------------------
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)
#---------------------------------------------------
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
#---------------------Cookie-------------------------
# headers = {
#     'Cookie': '_octo=GH1.1.1129764190.1656060769; _device_id=eb1ad9938489c1fd77e8319286b9003b; user_session=Ud48bCnwNevd9VNoiDV6g7MtIwZznpgYiTPU28vzf1_AjwGU; __Host-user_session_same_site=Ud48bCnwNevd9VNoiDV6g7MtIwZznpgYiTPU28vzf1_AjwGU; logged_in=yes; dotcom_user=MelonGO; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FMacau; _gh_sess=uffCFobxdKimObghSEzRIskL8oHzgaS8pkOZq571d3FWO433UFzhrG6139TqMHIqJi4Jq8wEi30BHMaYRwDCzDhC7OKAs4K8THecjpFIjmQ2DMyXO9g9xZU128rK6KHpNVNppsTz1ujxcNQ1dPZdh031WBJzK0%2Ba18tnk1jVF2VGxXSu%2Fa%2BCLgu50dnuSVa4--RrL8zQbZADdSGk76--0NjDqZEMXq7OZyMr6gS6UA%3D%3D',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
# }
# r = requests.get('https://github.com', headers=headers)
# print(r.text)
#---------------------------------------------------
# cookies = '_octo=GH1.1.1129764190.1656060769; _device_id=eb1ad9938489c1fd77e8319286b9003b; user_session=Ud48bCnwNevd9VNoiDV6g7MtIwZznpgYiTPU28vzf1_AjwGU; __Host-user_session_same_site=Ud48bCnwNevd9VNoiDV6g7MtIwZznpgYiTPU28vzf1_AjwGU; logged_in=yes; dotcom_user=MelonGO; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FMacau; _gh_sess=uffCFobxdKimObghSEzRIskL8oHzgaS8pkOZq571d3FWO433UFzhrG6139TqMHIqJi4Jq8wEi30BHMaYRwDCzDhC7OKAs4K8THecjpFIjmQ2DMyXO9g9xZU128rK6KHpNVNppsTz1ujxcNQ1dPZdh031WBJzK0%2Ba18tnk1jVF2VGxXSu%2Fa%2BCLgu50dnuSVa4--RrL8zQbZADdSGk76--0NjDqZEMXq7OZyMr6gS6UA%3D%3D'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get('http://github.com', cookies=jar, headers=headers)
# print(r.text)
#---------------------Session--------------------------
# s = requests.Session()
# s.get('https://httpbin.org/cookies/set/number/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)
#----------------------SSL-----------------------------
# urllib3.disable_warnings()
# logging.captureWarnings(True)
# response = requests.get('https://ssr2.scrape.center/', verify=False)
# #response = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)
#----------------------Timeout----------------------
# r = requests.get('https://httpbin.org/get', timeout=(5,30))
#-----------------------Auth------------------------
# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# # r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)
#-----------------------Proxy------------------------
# proxies = {
#   'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# }
# requests.get('https://httpbin.org/get', proxies=proxies)
#---------------------------------------------------
# proxies = {'https': 'http://user:password@10.10.1.10:3128/',}
# requests.get('https://httpbin.org/get', proxies=proxies)
#---------------------------------------------------
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://httpbin.org/get', proxies=proxies)
#---------------------------------------------------

# url = 'https://httpbin.org/post'
# data = {'name': 'germey'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)


















