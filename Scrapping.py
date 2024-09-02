import requests
from bs4 import BeautifulSoup
import re
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
dec = soup.find("p",class_="description card-text")
print(dec.string)
print("--------------------------------------------------------------------------------")
priceall = soup.find_all("h4",class_="price float-end card-title pull-right")
# for i in priceall:
#     print(i.text)
descall = soup.find_all("p",class_="description card-text")
print(descall[3].text)
#Strfind = soup.find_all(string="Pavilion")
#print(Strfind)
data = soup.find_all(string = re.compile("Aspire"))
print(data)