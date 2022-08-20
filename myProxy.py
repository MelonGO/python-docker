proxy_1 = {'http': 'http://141.164.37.2:3128' ,'https': 'http://141.164.37.2:3128' }
proxy_2 = {}
proxy_3 = {'http': 'http://141.164.57.55:8787' ,'https': 'http://141.164.57.55:8787' }
proxy_4 = {'http': 'http://158.247.234.118:8787' ,'https': 'http://158.247.234.118:8787' }
proxy_5 = 'proxy_5'

proxy_pool = [proxy_1, proxy_2, proxy_3, proxy_4, proxy_5]

index = 0


def getCurrent():
	return None


def getNext():
	global index
	if index > 4 :
		index = 0
		nextProxy = proxy_pool[index]
	else:
		nextProxy = proxy_pool[index]
	index = index + 1
	return nextProxy