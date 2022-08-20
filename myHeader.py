
import random

#http://www.dianping.com/shop/jH0ScSRraqaCzsqS/review_all
Cookie = '__mta=141816461.1660964062368.1660964062368.1660964062377.2; fspop=test; _lxsdk_cuid=182b92c1432c8-0586f23922c5ba-1b525635-fa000-182b92c14324; _lxsdk=182b92c1432c8-0586f23922c5ba-1b525635-fa000-182b92c14324; _hc.v=01a05fb3-398d-a92e-9497-af465e85ce4c.1660964050; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1660964050; cy=4; cye=guangzhou; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1660964058; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1660964058; wed_user_path=163|0; wedchatguest=g165530077864061217; lgtoken=05dc7e549-13b0-4c5d-b214-dae070342650; WEBDFPID=uuz79z90y338522y01y015005v46u288817y07x411v97958157vu8v0-1661050467505-1660964067095SMYIGGQ75613c134b6a252faa6802015be905512021; dplet=7cbd24161cca041973dfa4b4a4d8cc76; dper=52d133157ed9cd5652efb9aa386c2a432e928e395c9f09a663dc316e71716335a604966d941cd90bec11f7391011611d67dd66abe2d79746106f0948a618bbccf8de69352d85c7fffa51819c9b94df720d880728e7946dffc727399fb80bf1e1; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6981982693; ctu=c24d9f2d8f056fe3b1bd3d4b748d21cc6f2cbddd18bd478399d4e6561de9c122; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1660964088; _lxsdk_s=182b92bf694-f2-6c7-ffb%7C%7C297'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
User_Agent_1 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.82 Safari/537.36'


referer_1 = 'https://www.dianping.com/guangzhou/ch55/g163'
referer_2 = ''

referer = [referer_1, referer_2]


def random_ip():
    a=random.randint(1, 255)
    b=random.randint(1, 255)
    c=random.randint(1, 255)
    d=random.randint(1, 255)
    return (str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))

def getHeader(referer):
	if referer == 0:
		headers={
			'Accept-Language':'zh-CN,zh;q=0.9',
			'host':'www.dianping.com',
			'User-Agent': User_Agent,
			'X-Forwarded-For': random_ip(),
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'Cookie': Cookie,
		}
		return headers

	if referer == 1:
		headers={
			'Accept-Language':'zh-CN,zh;q=0.9',
			'host':'www.dianping.com',
			'referer': referer_1,
			'User-Agent': User_Agent,
			'X-Forwarded-For': random_ip(),
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'Cookie': Cookie,
		}
		return headers

	headers={
		'Accept-Language':'zh-CN,zh;q=0.9',
		'User-Agent': User_Agent,
		'X-Forwarded-For': random_ip(),
		'referer': referer,
		'host':'www.dianping.com',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Cookie': Cookie,
	}

	return headers