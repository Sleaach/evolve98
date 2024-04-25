import requests
from bs4 import BeautifulSoup
def crypto():
 try:
  urlsorgu = input("Birim: ").upper()
 
 #BTC
  url = f"https://www.google.com/finance/quote/BTC-{urlsorgu}?hl=tr"

  sayfa = requests.get(url)

  html = BeautifulSoup(sayfa.content, "html.parser")

  btc = html.find("div",class_="YMlKec fxKbKc").getText()
 

 #ETH
  url1 = f"https://www.google.com/finance/quote/ETH-{urlsorgu}?hl=tr"

  sayfa1 = requests.get(url1)

  html1 = BeautifulSoup(sayfa1.content, "html.parser")

  eth = html1.find("div",class_="YMlKec fxKbKc").getText()
 


 #DOG
  url2 = f"https://www.google.com/finance/quote/DOGE-{urlsorgu}?hl=tr"

  sayfa2 = requests.get(url2)

  html2 = BeautifulSoup(sayfa2.content, "html.parser")

  dogecoin = html2.find("div",class_="YMlKec fxKbKc").getText()
 
  print(f"""
BTC/{urlsorgu} {btc}
ETH/{urlsorgu} {eth}
DOGECOIN/{urlsorgu} {dogecoin}
""")

 except Exception as ex:
  print(f"Bir hata oluştu {ex}")
