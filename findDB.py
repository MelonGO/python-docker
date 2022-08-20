import myHeader
import pymongo

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'wedding'
MONGO_COLLECTION_NAME = 'shops'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['wedding']
collection = db['shops']

commentsDic = {
	'1' : 'comment_1',
	'2' : 'comment_2',
	'3' : 'comment_3',
}


data = {
'name': 'shop_1',
'total': 12345,
'price': 5000,
'score': 'good',
'comments':{},
}


def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)

def find_data(name, page):
    data = collection.find_one({'name':name})
    if data:
        print(data)
        if str(page) in data['comments'].keys():
            return 'exist'
        else:
        	return 'No'

# save_data(data)
# data = collection.find({'name': None})


# data = collection.find()
# total = 0
# for x in data:
#     print(x['name'])
# #     print(x['total'])
# #     print(x['price'])
# #     print(x['score'])
#     n = 0
#     for c in x['comments'].keys():

#         # print('Page '+ c)
#         k = 0
#         for i in x['comments'][c]:
#             if i != '':
#                 k = k + 1

#         n = n + k
#     print('本店有：' + str(n))
#     total = total + n
# print('一共有：' + str(total))

data = collection.find()
total = 0
for x in data:
    print(x['name'])
    total = total + 1
print(total)

# data = collection.find_one({'name':'山海视觉高端婚纱摄影(白云店)'})
# print(data['name'])
# print(data['total'])
# print(data['price'])
# print(data['score'])
# for x in data['comments']:
#     print(x)
#     for i in data['comments'][x]:
#         lines = i.split('\r\n')
#         print(lines)


# data = find_data('shop_1')
# comments = 'hahahahaha'
# each_page = 1
# if comments != None:
# 	data['comments'][str(each_page)] = comments
# 	save_data(data)

# collection.delete_one({'name': 'shop_1'})

# collection.delete_one({'name': None})
# collection.delete_many({})



