from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
# dbsparta : 데이터베이스 이름
# users : collections 에 들어갈 테이블 이름
# .insert_one
db.users.insert_one({'name': '덤블도어', 'age': 116})
db.users.insert_one({'name': '맥고나걸', 'age': 85})
db.users.insert_one({'name': '스네이프', 'age': 60})
db.users.insert_one({'name': '해리', 'age': 40})
db.users.insert_one({'name': '허마이오니', 'age': 40})
db.users.insert_one({'name': '론', 'age': 40})


