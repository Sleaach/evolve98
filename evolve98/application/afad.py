from bs4 import BeautifulSoup
import requests
def afad():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    re = requests.get(url)
    soup = BeautifulSoup(re.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    for i, row in enumerate(rows[1:11], start=1):  
        cells = row.find_all("td")

        
        location = cells[6].text.strip()
        magnitude = cells[5].text.strip()
        depth = cells[3].text.strip()
        date = cells[0].text.strip()
        print(f"""
{i}. Deprem Bilgisi:
Yer: {location}
Büyüklük: {magnitude}
Derinlik: {depth}
Tarih: {date}
""")
