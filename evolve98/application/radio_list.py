import requests
from bs4 import BeautifulSoup
def radiolist():
 try:
    url = "https://radyodelisi.blogspot.com/2019/01/turk-radyolari-2019-guncel-ip-adresleri.html"
    sayfa = requests.get(url)
    html = BeautifulSoup(sayfa.content, "html.parser")
    post_body = html.find("div", class_="post-body")
    
    if post_body:
        print(post_body.getText())

 except Exception as e:
    print(f"Bir hata oluştu: {e}")
