from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# name 이 덤블도어인 한 사람의 나이를 190으로 update 하라
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 190}})

# 여러 사람의 정보 바꾸기
db.users.update_many({'name': '허마이오니'}, {'$set': {'age': 20}})