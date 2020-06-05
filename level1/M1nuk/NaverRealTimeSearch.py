import requests
import os
from bs4 import BeautifulSoup
from time import sleep

os.system('color E')

# print('\033[33m' )

while True:
    os.system('cls')
    headers = {'referer': 'https://www.naver.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    req = requests.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main', headers=headers)
    pageSorce = req.text
    soup = BeautifulSoup(pageSorce, 'html.parser')
    rankCount = 0

    while (rankCount < 20):
        searchWord = soup.select('span.item_title_wrap > span.item_title')[rankCount]
        rank = soup.select('div > span.item_num')[rankCount]
        print(str(rank.get_text()).zfill(2) + ' ' + searchWord.get_text())
        rankCount = rankCount + 1

    sleep(10)