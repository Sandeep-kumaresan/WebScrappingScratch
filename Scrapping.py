import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
# tag = soup.header
# atb = tag.attrs
# print(atb["role"])
tag = soup.header.div.a.button.span
print(tag.string)
price = soup.find("h4",{"class":"price float-end card-title pull-right"})
print(price.string)