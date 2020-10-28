import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# db 정보 저장
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
data = requests.get('https://comic.naver.com/webtoon/list.nhn?titleId=651673', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# user.Agent
# javascript
# 개발자 모드
trs = soup.select('#content > table.viewList > tr')

# 제목, 제목 url ,이미지 url,하이퍼링크, 별점, 등록
for tr in trs:

    img_tag = tr.select_one('td > a > img')
    if img_tag is None:
        continue
    img = img_tag['src']

    title_tag = tr.select_one('td.title > a')
    if title_tag is None:
        continue
    title = title_tag.text
    url = title_tag['href']

    star_tag = tr.select_one('td > strong')
    if star_tag is None:
        continue
    star = star_tag.text

    reg_tag = tr.select_one('td.num')
    if reg_tag is None:
        continue
    reg = reg_tag.text


    data = {
        'img': img,
        'title': title,
        'url': url,
        'star': star,
        'reg': reg
    }

    db.webtoons.insert_one(data)






