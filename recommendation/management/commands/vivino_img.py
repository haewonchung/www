# Thanks to @kinghong97 for his work on data scraping from online wine marketplace

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'authority': 'www.vivino.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'x-requested-with': 'XMLHttpRequest',
    'scheme': 'https',
    'charset': 'utf-8',
    'cache-control': 'max-age=0',
    'accept-encoding': 'gzip, deflate, br',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': ''
}

df = pd.read_table('../../../../../../Wine.csv', sep=',')
# print(df['Link'])
# response = requests.get(
#     df['Link'][0],
#     headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# img = soup.select('picture.bottleShot')
# print(img[0].find_all('img')[0]['src'])
img_list = []
for i in df['Link']:
    response = requests.get(
        i,
        headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.select('picture.bottleShot')
    img_list.append(img[0].find_all('img')[0]['src'])
    print(img[0].find_all('img')[0]['src'])
    time.sleep(3)


df.insert(2, 'Img', img_list)
df.to_csv('wine.csv', index=False, encoding='utf-8')