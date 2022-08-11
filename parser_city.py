from bs4 import BeautifulSoup
import requests
import csv
import pprint
import pandas as pd
import re
import lxml

url = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%9A%D0%B8%D1%80%D0%B3%D0%B8%D0%B7%D0%B8%D0%B8'
req = requests.get(url)
src = req.text
res = []
r = []

soup = BeautifulSoup(src, 'lxml')

#TABLE
table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td]
    if row:
        res.append(row)

#LINK IN TABLE
city_href = table.find_all('a')
for a in city_href:
    col = a.get("href")
    if col:
        r.append(col)

# ALL LINK-CITY
city_link=[r[5], r[9], r[13], r[16], r[19], r[23], r[24], r[25], r[29], r[31], r[34], r[37], r[38], r[41], r[42], r[44], r[45], r[46], r[48], r[50], r[53], r[55], r[56], r[58], r[59], r[62], r[64], r[67], r[68], r[69], r[73]]


#PANDAS
df = pd.DataFrame(res,columns=('RUS','KGZ','FLAG','OLD NAME','STATUS SITY','2009','2019','STATUS','REGION',))
df['LINK']=city_link
df.drop(df.columns[2],axis=1,inplace=True)
df.to_csv('city2.csv',sep=';')

