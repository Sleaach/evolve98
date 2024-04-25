import feedparser
from bs4 import BeautifulSoup
def news():
    print("""TV Liste:

TRT HABER
CNN (US)
CNN TÜRK
NTV
    """)
    tv = input("TV: ").lower().strip()

    try:
        if tv in ["trt", "cnnturk", "ntv", "cnn"]:
            nfor = int(input("Adet: "))

            if tv == "trt":
                rss_url = 'https://www.trthaber.com/sondakika_articles.rss'
            elif tv == "cnnturk":
                rss_url = 'https://www.cnnturk.com/feed/rss/all/news'
            elif tv == "ntv":
                rss_url = 'https://www.ntv.com.tr/son-dakika.rss'
            elif tv == "cnn":
                rss_url = "http://rss.cnn.com/rss/edition.rss"

            feed = feedparser.parse(rss_url)

            for i, entry in enumerate(feed.entries[:nfor], 1):
                if 'description' in entry:
                    haber_basligi = BeautifulSoup(entry.description, 'html.parser').get_text()
                    print(f"\n{i}. {haber_basligi}\n\033[36m{entry.link}\n\033[0m")
                else:
                    print(f"\n{i}. Haber başlığı alınamadı.\n\033[36m{entry.link}\n\033[0m")

        else:
            print("\nGeçersiz TV.")

    except Exception as e:
        print(f"\nBir Hata Oluştu: {e}")
