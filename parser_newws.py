# coding=utf-8
import json
from urllib.request import urlopen

lim = input('Лимит новостей - ')
las = input('Дата - ')
ye = input('До какого года - ')

url = f"http://newsline.kg/getNews.php?limit={lim}&last_dt={las}%{ye}:57:33.933739"
response = urlopen(url)
data = json.loads(response.read())['data']


with open("data2.json", "w", encoding='utf-8') as f:
   json.dump(data, f, indent=4, ensure_ascii=False)







