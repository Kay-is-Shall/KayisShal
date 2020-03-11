import requests
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser');
list = []
news = {}

for headline in obj.find_all('div',class_='teaser_conten1'):
    news['Kategori'] = json.dumps(headline.find('h1').text)
    news['Judul'] = json.dumps(headline.find('h2').text)
    news['Waktu Publish'] = json.dumps(headline.find('div', class_='date').text)
    date = datetime.now()
    dt_string = date.strftime("%A, %d %B %Y %H:%M:%S")
    news['Waktu Ambil'] = dt_string
    temp = (str(news))
    list.append(temp)
    with open('headlinekayis.json', 'w') as file:
        json.dump(list, file, indent=4)

