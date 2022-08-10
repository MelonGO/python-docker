import httpx

import asyncio

#--------------------GET----------------------------
# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)
#---------------------------------------------------
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
# }
# response = httpx.get('https://httpbin.org/get', headers=headers)
# print(response.text)
#---------------------------------------------------
# client = httpx.Client(http2=True)
# response = client.get(
#     'https://spa16.scrape.center/')
# print(response.text)
#---------------------------------------------------
# with httpx.Client() as client:
#     response = client.get('https://httpbin.org/get')
#     print(response)


# client = httpx.Client()
# try:
#     response = client.get('https://httpbin.org/get')
# finally:
#     client.close()
#---------------------------------------------------
# url = 'http://httpbin.org/headers'
# headers = {'User-Agent': 'my-app/0.0.1'}
# with httpx.Client(headers=headers) as client:
#     r = client.get(url)
#     print(r.json()['headers']['User-Agent'])
#---------------------------------------------------
# client = httpx.Client(http2=True)

# response = client.get(
#     'https://httpbin.org/get')
# print(response.text)
# print(response.http_version)
#---------------------------------------------------

#---------------------------------------------------
# async def fetch(url):
#     async with httpx.AsyncClient(http2=True) as client:
#         response = await client.get(url)
#         print(response.text)

# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(fetch('https://httpbin.org/get'))
#---------------------------------------------------










