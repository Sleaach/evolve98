import requests
from bs4 import BeautifulSoup
from colorama import Fore
def onion():
    search = input("Onion: ")
    url = f"https://ahmia.fi/search/?q={search}"
    rq = requests.get(url)
    soup = BeautifulSoup(rq.content, "html.parser")
    results = soup.find_all("li", class_="result")[:21]  
    
    for result in results:
        title = result.find("a").text
        link = result.find("a")["href"]
        print(f"Title: {title}\n{Fore.LIGHTBLUE_EX}Link: {link}{Fore.RESET}")
