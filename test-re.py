import re

#--------------------match--------------------------
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())
#---------------------------------------------------
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
#---------------------------------------------------
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())
#-------------------非贪婪匹配-------------------------
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
#---------------------------------------------------


#-----------------search----------------------------
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
#---------------------------------------------------


html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''
#---------------------------------------------------
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S) 
# if result:  
#     print(result.group(1), result.group(2))
# #齐秦 往事随风
#---------------------------------------------------
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:  
#     print(result.group(1), result.group(2))
# #任贤齐 沧海一声笑
#---------------------------------------------------
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
# if result:  
#     print(result.group(1), result.group(2))
# #beyond 光辉岁月
#---------------------------------------------------

#-------------------findall-------------------------
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)  
# print(type(results))  
# for result in results:  
#     print(result)  
#     print(result[0], result[1], result[2])
#---------------------------------------------------

#--------------------sub----------------------------
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)
#---------------------------------------------------
# results = re.findall('<li.*?>\s*?(<a.*?>)?\s?(\w+)\s?(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])
# # 一路上有你
# # 沧海一声笑
# # 往事随风
# # 光辉岁月
# # 记事本
# # 但愿人长久
#---------------------------------------------------
# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())
#---------------------------------------------------

#-------------------compile-------------------------
# content1 = '2019-12-15 12:00'
# content2 = '2019-12-17 12:55'
# content3 = '2018-12-22 13:21'
# pattern = re.compile('\d{2}:\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)

#---------------------------------------------------




#---------------------------------------------------




#---------------------------------------------------



#---------------------------------------------------




#---------------------------------------------------




#---------------------------------------------------