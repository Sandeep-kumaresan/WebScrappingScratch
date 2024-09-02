import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
names = soup.find_all("a",class_ = "title")
namelist = []
for i in names:
    namelist.append(i.text)
desc = soup.find_all("p",class_ = "description card-text")
desclist = []
for i in desc:
    desclist.append(i.text)
price = soup.find_all("h4",class_="price float-end card-title pull-right")
pricelist = []
for i in price:
    pricelist.append(i.text)
rating = soup.find_all("p",class_="review-count float-end")
ratinglist = []
for i in rating:
    ratinglist.append(i.text)
print(namelist)
print(desclist)
print(pricelist)
print(ratinglist)