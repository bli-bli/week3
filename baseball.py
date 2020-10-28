import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 야구 순위, 팀이름
trs = soup.select('#regularTeamRecordList_table > tr')

# 0.5 와의 크기를 비교하기위해 rate.text를 부동소숫점형(float)으로 강제 형변환
for tr in trs:
    rank = tr.select_one('th > strong').text
    team = tr.select_one('td.tm > div > span').text
    rate = tr.select_one('td > strong').text
    if rank is not None and float(rate) > 0.5:
        print(rank, team)
