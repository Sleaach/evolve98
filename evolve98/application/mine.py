import requests
from bs4 import BeautifulSoup
def mine():
 url = "https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/"
 geturl = requests.get(url)

 beau = BeautifulSoup(geturl.content, "html.parser")

 find = beau.find("span",class_= "value up").getText()

 print(f"\nALTIN (TL/GR) {find}")

 url = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
 geturl = requests.get(url)

 beau = BeautifulSoup(geturl.content, "html.parser")

 find = beau.find("span",class_= "value up").getText()

 print(f"Çeyrek Altın {find}\n")
