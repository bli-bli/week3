from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

# 검색엔진에 url을 직접 작성해서 해당 웹페이지의 정보를 불러오는 것과
# requests.get 의 방식으로 정보를 불러오는 것에는 차이가 있기 때문에 headers 를 같이 불여주어야함
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20180327',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링: 검색엔진에서 검색결과를 가져가는 것
# 웹 스크래핑: 특정 웹사이트에서 특정 정보를 긁어가는 것 / beautifulsoup4 : HTML 코드를 쉽게 스크래핑 해오기 위한 도구
# 카피 셀렉터

# .text: 가져온 html의 text만 가져오기
# ['href']: 속성 가져오기
# is not None: None을 쓸 때는 이렇게 작성해야한다
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    rank = tr.select_one('td.ac > img')
    title = tr.select_one('td.title > div.tit5 > a')
    point = tr.select_one('td.point')

    if rank is not None:
        print(rank['alt'], title.text, point.text)

        dic = {
            'rank': rank['alt'],
            'title': title.text,
            'point': point.text
        }
        db.movies.insert_one(dic)






