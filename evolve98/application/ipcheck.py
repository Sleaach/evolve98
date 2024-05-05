import requests
import os
def ipch():
 try:
  os.system('clear||cls')
  url1 = input("IP: ")
  url = f"http://ip-api.com/json/{url1}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
  os.system('clear||cls')
  response = requests.get(url).json()
  print("Ip:", response["query"])
  print("Durum:", response["status"])
  print("Bölge:", response["continent"])
  print("Ülke:", response["country"])
  print("Ülke Kodu:", response["countryCode"])
  print("Şehir:", response["city"])
  print("Plaka:", response["region"])
  print("Zaman:", response["timezone"])
  print("Sağlayıcı:", response["org"])
  print("Zip", response["zip"])
  print("Proxy:", response["proxy"])
 except Exception as e:
  print(e)