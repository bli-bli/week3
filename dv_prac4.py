import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:

    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:

        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = movie.select_one('td.point').text
        # print(rank, title, star)

        doc = {
            'rank': rank,
            'title': title,
            'star': star
        }
        # db.movies.insert_one(doc)
# 월-E 평점을 가져온 뒤 그것과 같은 평점의 영화 제목들을 가져오기
wall_star = db.movies.find_one({'title': '월-E'})
target = wall_star['star']

db.movies.update_many({'star': target}, {'$set': {'star': '0'}})