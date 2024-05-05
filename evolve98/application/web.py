import requests
from bs4 import BeautifulSoup
import time
def web():
    try:
        w = input("Web URL'sini girin: ")
        response = requests.get(w)

        if response.status_code == 200:
            print("\nİstek başarılı, web sayfasının içeriği:\n")
            time.sleep(2)
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
        else:
            print(f"Hata kodu: {response.status_code}")
    except Exception as e:
        print(f"Hata oluştu: {e}")
