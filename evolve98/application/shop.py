import requests
from bs4 import BeautifulSoup
def shop():
    url = "https://www.trendyol.com/sr?fl=encokonecikanurunler&pi=2"

    re = requests.get(url)

    sou = BeautifulSoup(re.content, "html.parser")

    find1 = sou.find_all("h3")
    find2 = sou.find_all("div", class_="prc-box-dscntd")

    for index, (title_element, price_element) in enumerate(zip(find1, find2)):
        
        title_text = title_element.get_text(strip=True)
        price_text = price_element.get_text(strip=True)

        print(f"\n\033[37mÜrün {index + 1}: {title_text} - Fiyat: \033[32m{price_text}")

