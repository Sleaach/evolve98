import feedparser
from bs4 import BeautifulSoup
def customrss():
 nfor = int(input("Adet: "))
 url = input("Url: ")
 feed = feedparser.parse(url)
 for i, entry in enumerate(feed.entries[:nfor], 1):
    if 'description' in entry:
        haber_basligi = BeautifulSoup(entry.description, 'html.parser').get_text()
        print(entry.published)
        print(f"\n{i}. {haber_basligi}\n\033[36m{entry.link}\n\033[0m")
    else:
        print(f"\n{i}. Haber başlığı alınamadı.\n\033[36m{entry.link}\n\033[0m")
