import requests
from lxml import etree

url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'}

res = requests.get(url, headers=headers)
e = etree.HTML(res.text)
e
nos: list = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names: list = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams: list = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores: list = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

names.insert(0, '姓名')
teams.insert(0, '球队')

with open('nba.txt', 'w', encoding= 'utf-8') as f:
    for no, name, team, score in zip(nos, names, teams, scores):
        f.write(f"{no} {name} {team} {score}\n")
