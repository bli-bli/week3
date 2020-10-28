from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 특정 값을 제외하고 출력하고 싶은 경우
list(db.users.find({}))
all_users = list(db.users.find({}, {'_id':0}))

for user in all_users:
    print(user)
    
# name 이 스네이프인 사람만 찾고 싶은 경우
list(db.users.find({}))
all_users = list(db.users.find({'name':'스네이프'}, {'_id':0}))

for user in all_users:
    print(user)

# 지정된 하나의 값만 id 값은 제외하고 찾고 싶은 경우
user = db.users.find_one({'name':'덤블도어'}, {'_id':False})
print(user)



