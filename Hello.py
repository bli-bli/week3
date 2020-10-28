# 변수, 자료형, 함수, 조건문, 반복문
# 파이썬에서는 _ 를 이용하여 변수이름을 많이 설정한다.

# 자료형을 선언해줄 필요 없음. 숫자와 문자를 연산하지 못한다
a = '2'
first_name = 'sparta'

print(a+first_name)

# 리스트는 데이터 추가시 append
a_list = ['사과', '배', '수박']
print(a_list[0])
a_list.append('키위')
print(a_list)

# 딕셔너리는 데이터 추가시 [''] =
a_dict = {'name':'bob', 'age': 24}
a_dict['height'] = 180
print(a_dict)

# 함수
def sum(a,b):
    return a+b

result = sum(1,2)
print(result)

# 조건문
def is_adult(age):
    if age > 20:
        print('성인이네요')
    else:
        print('청소년이네요')

is_adult(23)
is_adult(10)

# 반복문
fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

# 예제 - 입력받은 과일의 개수
def count_fruit(fruit_name):
    cnt = 0
    for fruit in fruits:
        if fruit == fruit_name:
            cnt += 1
    return print(cnt)

count_fruit('귤')

professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

for wizard in professor_wizards:
    if wizard['age'] > 100:
        print(wizard['name'])



