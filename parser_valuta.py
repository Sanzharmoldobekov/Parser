from bs4 import BeautifulSoup
import requests
import csv
import pprint
import pandas as pd
import re
import lxml

url = 'https://www.akchabar.kg/ru/exchange-rates/'
req = requests.get(url)
src = req.text
res = []

soup = BeautifulSoup(src, 'lxml')
#parser table
table = soup.find('table', {'id': 'rates_table'})
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td ]
    if row:
        res.append(row)
#pandas
tim = soup.find("div",id='rates').find('strong')
df = pd.DataFrame(res,columns=('','USD','USD','EURO','EURO','RUB','RUB','KZT','KZT'))
df.to_csv(f'{datetime.now().date()}_valut.csv', sep=';')
