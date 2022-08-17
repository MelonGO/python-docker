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
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
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

temp = '''

    </div>
</div>
        <!--页面主体-->
        <div class="review-list-container">
            <!--商户信息-->
        <div class="review-shop-wrap">
    <div class="shop-info clearfix">
        <h1 class="shop-name">悦摄视觉婚纱摄影工作室</h1>
    </div>
    <div class="rank-info">
        <div class="nebula_star ">
            <div class="star_icon">
                <span class="star star_50"></span>
                <span class="star star_50"></span>
                <span class="star star_50"></span>
                <span class="star star_50"></span>
                <span class="star star_50"></span>
            </div>
                <div class="star_score score_50">4.90</div>
        </div>
        <span class="reviews">185条评价</span>
        <span class="price">人均：6005元</span>
	        <span class="score">
	                <span class="item">摄影：4.90</span>
	                <span class="item">造型：4.90</span>
	                <span class="item">服务：4.90</span>
            </span>
    </div>
    <div class="address-info">
        地址:&nbsp;<bb class="anj11"></bb><bb class="ancwq"></bb>大道中风樯<bb class="ankd7"></bb>意<bb class="anut5"></bb>3栋<bb class="an36q"></bb><bb class="anqp8"></bb>楼3110<bb class="ans7k"></bb>（风樯行009进入）
    </div>
	    <div class="phone-info">
            电话:&nbsp;<cc class="jqezn"></cc><cc class="jqgqc"></cc><cc class="jqgqc"></cc><cc class="jqgqc"></cc><cc class="jq6zb"></cc><cc class="jqgqc"></cc><cc class="jqcq7"></cc><cc class="jqotd"></cc>1<cc class="jqgqc"></cc>-1<cc class="jq30j"></cc><cc class="jqezn"></cc>1<cc class="jqgqc"></cc>1
        </div>
    <div class="more-wrap">
        <div class="qcode">
            <div class="qcode-wrap">
                <img src="http://p0.meituan.net/dpgroup/8db53f85b5a3e72b79b12df8abeec0572506.png" alt="二维码">
                <div class="qcode-r">
'''
#---------------------------------------------------

results = re.findall('<span class="score">\s+<span class="item">(.*?)</span>\s+<span class="item">(.*?)</span>\s+<span class="item">(.*?)</span>\s+</span>', temp, re.S) 
if results:
	for result in results:
		print(result)
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