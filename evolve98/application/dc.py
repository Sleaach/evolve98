import requests
from bs4 import BeautifulSoup
url = 'https://discordstatus.com/'
def dc():
 response = requests.get(url)
 if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    span_tags = soup.find('span', id='uptime-percent-rhznvxg4v7yh')
    span2_tags = soup.find('span', id='uptime-percent-r3wq1zsx72bz')
    span3_tags = soup.find('span', id='uptime-percent-x7rnz0t7dpnp')
    span4_tags = soup.find('span', id='uptime-percent-354mn7xfxz1h')
    span4_tags = soup.find('span', id='uptime-percent-3y468xdr1st2')
    print("----DISCORD SERVER STATUS----")
    print("API: ", span_tags.text)
    print("Media Proxy: ", span2_tags.text)
    print("Gateway: ",span3_tags.text)
    print("Push Notifications: ",span4_tags.text)
    print("Search: ",span4_tags.text)
 else:
    print("Sayfa yüklenirken bir hata oluştu. Hata kodu:", response.status_code)