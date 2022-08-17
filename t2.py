proxy_1 = 'proxy_1'
proxy_2 = 'proxy_2'
proxy_3 = 'proxy_3'
proxy_4 = 'proxy_4'
proxy_5 = 'proxy_5'

proxy_pool = [proxy_1, proxy_2, proxy_3, proxy_4, proxy_5]

index = 0


def getNext():
	global index
	if index > 4 :
		index = 0
		nextProxy = proxy_pool[index]
	else:
		nextProxy = proxy_pool[index]
	index = index + 1
	return nextProxy
