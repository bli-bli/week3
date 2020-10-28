from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# db 정보 저장
db = client.dbsparta

# 입력
db.users.insert_one({'name': '덤블도어', 'age': 116})
db.users.insert_one({'name': '맥고나걸', 'age': 85})
db.users.insert_one({'name': '스네이프', 'age': 60})
db.users.insert_one({'name': '해리', 'age': 40})
db.users.insert_one({'name': '허마이오니', 'age': 40})
db.users.insert_one({'name': '론', 'age': 40})

# 조회
users = list(db.users.find({'age' : 40 ,'_id' : False}))




# python 에서 for 문을 사용하는 이유
# iterable : 프로그래밍을 해놓으면 코드로 존재하기는 하지만 이는 메모리에 올라가 있는 것은 아니다. ex) r = range(5)
# 만약 메모리에 올리고 싶다면 2가지 형식으로 메모리에 저장해주어야 한다.
# ex1) ls = list(r) / ex2) list(db.users.find({})) / ex3) for user in users: print(user)

# condition dictionary
# projection dictionary (빼고 주세요) ex) _id : False

# find(리스트 형태로 가져옴) , find1(딱 하나만 값이 존재할것이라 생각하는 경우)

