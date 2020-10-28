import requests

# interpreter setting -> python interpreter -> requests 라이브러리 설치
# requests 라이브러리를 사용하면 ajax call 을 굉장히 쉽게 할 수 있음
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

city_air = response_data.json()

rows = city_air['RealtimeCityAir']['row']

for row in rows:
    if row['PM10'] < 50:
        print(row['MSRSTE_NM'],row['PM10'])




