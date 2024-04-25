import requests
from bs4 import BeautifulSoup
def exchange():
 url = f"https://www.google.com/finance/quote/GARAN:IST?hl=tr"

 sayfa = requests.get(url)

 html = BeautifulSoup(sayfa.content, "html.parser")

 garanti = html.find("div",class_="YMlKec fxKbKc").getText()
 



 url = f"https://www.google.com/finance/quote/AKBNK:IST?hl=tr"

 sayfa = requests.get(url)

 html = BeautifulSoup(sayfa.content, "html.parser")

 akbnk = html.find("div",class_="YMlKec fxKbKc").getText()
 print(f"""\n
AKBNK {akbnk}
GARAN {garanti}
""")
