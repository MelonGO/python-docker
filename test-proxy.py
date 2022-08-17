import requests

# proxy_1 = '158.247.233.4:3128'
# proxy_2 = '141.164.37.2:3128'
# proxy_3 = '45.32.48.233:3128'
# proxy_4 = '158.247.233.200:3128'
# proxy_5 = '45.77.11.139:3128'

proxy_1 = '158.247.234.118:3128'
proxy_2 = '141.164.57.55:3128'
proxy_3 = '45.32.122.144:3128'
proxy_4 = '149.28.156.107:3128'
proxy_5 = '45.77.11.139:3128'

proxies = {
    'http': 'http://' + proxy_5,
    'https': 'http://' + proxy_5,
}
try:
    response = requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)