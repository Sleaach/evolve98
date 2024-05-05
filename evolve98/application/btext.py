import requests
from bs4 import BeautifulSoup

def btext():
 while True:
        main = input("URL: ")

        if main == "q":
                break
            
        response = requests.get(main)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, "html.parser")
                
            print(soup.get_text())
        else:
                print('İstek başarısız oldu:', response.status_code)
