import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
table = soup.find("table",class_="table table-sm table-hover screenertable")
head = table.find_all("th")
# print(head)
heading = []
for i in head:
    title = i.text
    heading.append(title)

# print(heading)
df = pd.DataFrame(columns=heading)
print(df)
row = table.find_all("tr")
#print(row)
