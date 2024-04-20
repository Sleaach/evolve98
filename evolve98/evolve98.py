try:
 from pynput.keyboard import Key, Controller
 import time
 import psutil
 import datetime
 from colorama import Fore,Style
 import platform
 import requests 
 from bs4 import BeautifulSoup
 import random
 import string
 import qrcode
 import socket
 import os
 import subprocess
 import smtplib
 from email.mime.text import MIMEText
 from email.mime.multipart import MIMEMultipart
 import speedtest
 import math
 import sympy as sp
 import pygame
 import pandas as pd
 import vlc
 import feedparser
 from requests_oauthlib import OAuth1Session
 import json
 import ctypes
 import uuid
 import webbrowser
 import whois
 import pyautogui
 import cv2
 from PIL import Image
 from pytube import YouTube
 import phonenumbers
 from phonenumbers import geocoder as pn_geocoder  
 from phonenumbers import carrier 
 from opencage.geocoder import OpenCageGeocode
 import google.generativeai as genai
 import calendar as c
except Exception as x:
 print(f"Kütüphaneler eksik veya düşük sürüm.\n {x}")

admin = False
tarih = datetime.datetime.now()
tarih_str = tarih.strftime("%Y-%m-%d %H:%M:%S")

red = False
yellow = False
blue = False
green = False
reset = False

ASCII_CHARS = '@%#*+=-:. ₺$£1u[̉ €];&¾~|{}0ß»«¢“”µ×·ª?^<>!'
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image
def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        if 0 <= pixel_value < 256: 
            # Check the length of ASCII_CHARS list and limit the index
            index = min(pixel_value // 25, len(ASCII_CHARS) - 1)
            ascii_str += ASCII_CHARS[index]
        else:
            ascii_str += ' '  # Use space character if pixel value is out of range
    return ascii_str
def video_to_ascii(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = resize_image(image)
        image = grayify(image)
        ascii_str = pixels_to_ascii(image)
        ascii_str = '\n'.join([ascii_str[i:i+image.width] for i in range(0, len(ascii_str), image.width)])
        print(ascii_str)
        time.sleep(0.1)
    cap.release()

def caleda():
    y = int(input("Yıl: "))
    m = int(input("Ay: "))
    print(f"\n,{Fore.GREEN}{c.month(y,m)}")

def help():
 print("""\n
userinfo: Kullanıcı hakkında bilgi verir.
sysinfo: Sistemi gözler.
date: Anlık tarihi gösterir.
calc: Hesap makinesi.
temp: Bileşenlerin sıcaklıklarını gösterir.
nick: Rasgele nick verir.
---------------------------------------
---------------------------------------
root: Yetkili kullanıcı yapar.
pwd: Mevcut çalışma dizinini gösterir.  
shut: Sistemi kapatır.
note: Not defterini açar.
notebook: Notları gösterir.
fx: Döviz Çevirici.
cls: Output temizler.
data: Veri yönetimi.
---------------------------------------
---------------------------------------
exit: Root kullanıcıdan çıkar.
news: Son dakika haberleri gösterir.
twt: Twitter'a post atar.
twthelp: Twitter'a post atma yollarını gösterir.
afad: Anlık deprem haberler.
---------------------------------------
---------------------------------------
en: Klavyeyi İngilizce yapar. (Sadece Windows)
shop: Trendyol'dan en popüler ürünleri listeler.
saving: Tasarruf moduna geçer ve belirli bir süre sonra sistemi kapatır.
mouse: İmlecin kordinatını verir.
---------------------------------------
---------------------------------------
gsm: fake numara üretir. (TR)
bilim: evrimagaci haberleri.
youtb: YouTube'dan video indirir.
cal: Takvim oluşturur.
onion: .onion Uzantılı dosyaları indexler.
btext: Text tabanlı web tarayıcısı.
---------------------------------------
---------------------------------------
cd: Mevcut dizini değiştirir.
pass: Rasgele şifre oluşturur.
qrcode: QR kod oluşturur.       
weather: Hava durumunu gösterir.
touch: Dosya oluşturur.
crypto: Kripto değerlerini gösterir.
mail: Mail gönderir. (Sadece Yandex)
shutdown: Sistemi kapatır.
---------------------------------------
---------------------------------------
reboot: Sistemi yeniden başlatır.
trash: Dosya veya veri siler.
ls: Bulunduğun dizindeki dosyaları gösterir.
find: Belirtilen konumda ve uzantıda dosyaları sıralar.
du: Dizinin boyutunu gösterir.
pomodoro: Pomodoro vakti.
stock: Borsa görüntüleyici.
---------------------------------------
---------------------------------------
scalc: Gelişmiş hesap makinesi.
mp3: Müzik çalar.
radio: Radio açar.
radiolist: Radio istasyonların URL'sini gösterir.
coal: Madenlerin değerlerini gösterir.
clean: Verilen dizin tamamen siler.
todo: Yapılacaklar listesi.
---------------------------------------
---------------------------------------
control: Sistemin sağlığını kontrol eder bileşikleri güvende tutar.
ascii: Video'u ascii şekline çevirir.
upd: Paketleri günceller.
upg: Paketleri yükseltir.
posi: Mouse hareket ettiğinde google sekmesi açar.
numcheck: Gsm sorgu. 
ai: 1.Seviye yapay zeka.

               
--EĞLENCE KOMUTLARI-- 
       
rainbow: Renkli top.
slot: Jackpot oyunu.
rulet: Rulet oyunu.
fp: Yazı Tura atar.

       
--NETWORK KOMUTLARI--
       
web: Web sitenin kaynak kodlarını gösterir.
speedtest: İnternet hızını ölçer.
search: Web Tarayıcısı.
mac: MAC adresini gösterir.
ip: IP adresini gösterir.
ping: Bağlantınızı kontrol eder.
domain: Domain kontrolü.
machange: Mac adresini değiştirir.
       


--RENK KOMUTLARI--
red
green
blue
yellow
reset
""")

def Machange():
    try:
     YeniMac = str(input("New Mac: "))
     İnterface = input("Interface: ")

     subprocess.call(["sudo", "ifconfig", İnterface, "down"])

     subprocess.call(["sudo", "ifconfig", İnterface, "hw", "ether", YeniMac])

     subprocess.call(["sudo", "ifconfig", İnterface, "up"])
 
     oncekimac = subprocess.check_output(["ifconfig"])

     yenimac = subprocess.check_output(["ifconfig"])

     if oncekimac == yenimac:
        print("Mac adresi değiştirme başarısız oldu.")
     else:
        print("Mac adresi değiştirildi. Yeni Mac: ", YeniMac)
    except Exception as e:
       print(f"Hata oluştu: {e}")

def task():
    tasks = []   

    while True:
        print("""
1. Görev Ekle
2. Görev Sil
3. Görev Görüntüle
4. Çıkış
        """)
        choice = input(": ")

        if choice == "1":
            while True:
                tass = input("Görev: ")
                if tass.lower() == "4":
                    break
                else:
                    tasks.append(tass) 

        if choice == "2":
            print("Silmek istediğin görevi yaz.")
            while True:
                delet = input("\nGörev: ")
                if delet.lower() == "4":
                    break
                try:
                    tasks.remove(delet)
                    print(f"Görev '{delet}' silindi.")
                except ValueError:
                    print(f"Görev '{delet}' bulunamadı. Lütfen tekrar deneyin.")

        if choice == "3":
            print("Görevler:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        if choice == "4":
           break

def rulet():
    color = ["Kırmızı", "Siyah", "Yeşil"]
    coin = 2000
    selectbahis = 0

    try:
        while True:
            if coin == 0:
                break
            print("Çıkmak için 'q'")
            print(f"coin: {coin}")
            main = int(input("\nBahis miktarı: "))
            if main == "q":
                break
            if coin >= main:
                selectbahis += main
                main2 = input("Bahis rengi (Kırmızı/Siyah/Yeşil): ").capitalize()  
                if main2 == "q":
                 break
                time.sleep(1.2)
                print("Bahisler kapanıyor, çark çevriliyor...")
                chose = random.choice(color)
                time.sleep(1.3)
                print(f"Çıkan Renk: {chose}")
                if main2 in color:
                    if chose == main2:
                        coin += main * 2  
                        print(f"{Fore.GREEN}KAZANDINIZ! Bakiyeniz: {coin}{Fore.RESET}")
                    else:
                        coin -= main  
                        print(f"{Fore.RED}KAYBETTİNİZ! Bakiyeniz: {coin}{Fore.RESET}")
                else:
                    print("Geçersiz renk seçimi.")
                    break
            else:
                print("Yetersiz bakiye.")
                break
    except Exception as e:
        print("Bir hata oluştu:", e)

def twt():
 print("'twthelp' kodunu çalıştırıp okuduğunuzdan emin olun.\n")
 consumer_key = input("API: ")
 consumer_secret = input("SECRET: ")
 mesaj = input("Post: ")
 payload = {"text": mesaj}

 request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
 oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

 try:
    fetch_response = oauth.fetch_request_token(request_token_url)
 except Exception as e:
   print(f"Bir hata oluştu: {e}")
    

 resource_owner_key = fetch_response.get("oauth_token")
 resource_owner_secret = fetch_response.get("oauth_token_secret")
 print("OAuth jetonunu aldım: %s" % resource_owner_key)



 base_authorization_url = "https://api.twitter.com/oauth/authorize"
 authorization_url = oauth.authorization_url(base_authorization_url)
 print("Lütfen buraya gidin ve yetkilendirin: %s" % authorization_url)
 verifier = input("PIN'i buraya yapıştırın: ")


 access_token_url = "https://api.twitter.com/oauth/access_token"
 oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
 oauth_tokens = oauth.fetch_access_token(access_token_url)

 access_token = oauth_tokens["oauth_token"]
 access_token_secret = oauth_tokens["oauth_token_secret"]

 oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

 response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

 if response.status_code != 201:
    raise Exception(
        "İstek bir hata döndürdü: {} {}".format(response.status_code, response.text)
    )

 print("Cevap kodu: {}".format(response.status_code))


 json_response = response.json()
 print(json.dumps(json_response, indent=4, sort_keys=True))

def twitterhelp():
   print("""Post atmak için gerekli işlemler:

1. Twitter hesabınız olması gerekiyor.
2. Bilgisayarınızdan Twitter hesabınıza girin.
2. Twitterdev sitesinden bir API istediğinizi belirtin.
3. API aldıktan sonra twt komutu yazarak uygulamayı açın.
4. Verilen API'i uygulamaya yapıştırın.
5. Gösterilen siteye tıklayın onay butonuna tıklayın.
6. Verilen doğrulama kodunu uygulamaya girin.
7. En son hangi postu atıcağınıza karar verin.
8. Eğer 201 yazısını görürseniz başarılı bir şekilde post atmış oluyorsunuz.
         """)

def youtb():
 try:
    link = input("Link: ")
    yt = YouTube(link)
    yr = yt.streams.get_highest_resolution()
    print("Video OK")
    yr.download(filename='video')
 except Exception as e:
  print(f"Hata! {e}")

def maden():
 url = "https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/"
 geturl = requests.get(url)

 beau = BeautifulSoup(geturl.content, "html.parser")

 find = beau.find("span",class_= "value up").getText()

 print(f"\nALTIN (TL/GR) {find}")

 url = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
 geturl = requests.get(url)

 beau = BeautifulSoup(geturl.content, "html.parser")

 find = beau.find("span",class_= "value up").getText()

 print(f"Çeyrek Altın {find}\n")

def kapat():
    osy = os.name
    try:
        if osy == "Linux":
         os.system("shutdown now")
        else:
            os.system("shutdown /s /f /t 0")  
    except Exception as e:
        print(f"\nSistem kapatma hatası: {e}\n")

def reboot():
    try:
        os.system("reboot now")  
    except Exception as e:
        print(f"\nSistem yeniden başlatma hatası: {e}\n")

def mail():
    try:
        # Kullanıcıdan bilgileri al
        email = input("Gönderen Mail: ")
        postsifre = input("Gönderen Şifre veya Uygulama Şifresi: ")
        send = input("Alıcı Mail Adresi: ")
        subjet = input("Konu: ")
        message = input("Mesaj: ")

        # E-posta içeriğini oluştur
        content = MIMEMultipart()
        content["From"] = email
        content["To"] = send
        content["Subject"] = subjet
        content.attach(MIMEText(message, "plain"))

        # SMTP bağlantısı oluştur
        mail = smtplib.SMTP("smtp.yandex.com", 587)
        mail.ehlo()
        mail.starttls()

        # Giriş yap
        mail.login(email, postsifre)

        # E-postayı gönder
        mail.sendmail(email, send, content.as_string())

        # Bağlantıyı kapat
        mail.quit()

        print("\nMail gönderildi.")
    except Exception as e:
        print(f"Bir hata oluştu. {e}")

def clear():
    isletim_sistemi = platform.system()

    if isletim_sistemi == "Windows":
        subprocess.call("cls", shell=True)
    elif isletim_sistemi in ["Linux", "Darwin"]:
        subprocess.call("clear", shell=True)
    else:
        print("Bu işletim sistemi desteklenmiyor.")

def upd():
    print(os.system("sudo apt update"))
    
def calculator():
    

    while True:
        print("\nişlem seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")

        secim = input(": ")

        if secim == "5":
            time.sleep(1)
            print("Hesap makinesi kapatılıyor.")
            time.sleep(1.5)
            break

        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")
            continue

        if secim == "1":
            sonuc = sayi1 + sayi2
        elif secim == "2":
            sonuc = sayi1 - sayi2
        elif secim == "3":
            sonuc = sayi1 * sayi2
        elif secim == "4":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                print("Hata: Sıfıra bölme hatası.")
                continue
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue

        print(f"Sonuç: {sonuc}")

def sysinfo():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    net_info = psutil.net_io_counters()
    operating_system = platform.system()
    cpuinfo = platform.processor()
    print("\nSistem Bilgileri:")
    print(f"İşletim sistemi: {operating_system}")
    print(f"CPU Mimarisi: {cpuinfo}")
    print(f"CPU Kullanımı: {Fore.GREEN}{cpu_percent}%{Style.RESET_ALL}")
    print(f"RAM Kullanımı: {Fore.BLUE}{ram_percent}%{Style.RESET_ALL}")
    print(f"Disk Kullanımı: {Fore.MAGENTA}{disk_percent}%{Style.RESET_ALL}")
    print(f"İşlemci Sayısı: {psutil.cpu_count(logical=False)} (Fiziksel)")
    print(f"Toplam Bellek: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Aktif Ağ Bağlantıları: {net_info.packets_sent} gönderilen, {net_info.packets_recv} alınan")

def get_temperatures():
    try:
        temp_info = psutil.sensors_temperatures()

        if 'coretemp' in temp_info:
            cpu_temp = temp_info['coretemp'][0].current
            print(f"CPU Sıcaklığı: {Fore.RED}{cpu_temp}°C{Style.RESET_ALL}")

        if 'radeon' in temp_info:
            gpu_temp = temp_info['radeon'][0].current
            print(f"GPU Sıcaklığı: {Fore.YELLOW}{gpu_temp}°C{Style.RESET_ALL}")

        if 'acpitz' in temp_info:
            other_temp = temp_info['acpitz'][0].current
            print(f"Diğer Bileşen Sıcaklığı: {Fore.CYAN}{other_temp}°C{Style.RESET_ALL}")

    except Exception as e:
        print(f"Sıcaklık okuma hatası: {e}")

def note():
    with open("note.txt", "a") as note:
            while True:
                notebook_entry = input("(Çıkmak için exit) Notebook: ")
                if notebook_entry == "exit":
                    print("\nNotebook uygulamasından çıkış yapıldı.")
                    break
                note.write(f"\n{notebook_entry}")
                
def notebook():
    with open("note.txt", "r") as note:
            content = note.read()
            print(f"\n{content}")

def doviz():
    apiurl = "https://v6.exchangerate-api.com/v6/a925a27db978233d2605c41e/latest/USD"

    bozulan = input("Bozulan döviz: ").upper()
    alinan = input("Alınan döviz: ").upper()

    try:
        miktar = float(input(f"Ne kadar {bozulan} bozdurmak istiyorsunuz?: "))
    except ValueError:
        print("Geçerli bir miktar girin. Örneğin: 100.50")
        return  
    sonuc = requests.get(apiurl)
    sonucjs = sonuc.json()

    if sonuc.status_code == 200:
        rates = sonucjs['conversion_rates']

        if alinan in rates and bozulan in rates:
            bozulan_kur = rates[bozulan]
            alinan_kur = rates[alinan]

            alinan_miktar = miktar / bozulan_kur * alinan_kur

            print(f"{miktar} {bozulan} = {alinan_miktar:.2f} {alinan}")
        else:
            print("Geçersiz döviz türü.")
    else:
        print(f"API'den veri alınamadı. Hata kodu: {sonuc.status_code}")

def generate_password():
    while True:
        try:
            hane = int(input("Hane: "))
            if hane > 0:
                break
            else:
                print("Lütfen pozitif bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    sifre = ""
    haneler = string.ascii_letters + string.digits + string.punctuation

    for i in range(hane):
        sifrecc = random.choice(haneler)
        sifre += sifrecc

    print(f"Oluşturulan şifre: {sifre}")

def qrcodde():
    try:
     veri = input("QR Kod oluşturulacak veriyi girin: ")
     dosya_yolu = input("QR Kod dosyasını kaydetmek istediğiniz yolu girin: ").strip().lower()

     if veri:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(veri)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(dosya_yolu)

        print(f"QR kodu oluşturuldu ve '{dosya_yolu}' olarak kaydedildi.")
     else:
        print("QR kodu oluşturulamadı.")
    except Exception as f: 
         print(f"Bir hata oluştu. {f}")

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

def isim_sec():
    try:
        with open("nick.txt", "r", encoding="utf-8") as dosya:
            isimler = dosya.readlines()

        if isimler:
            isimkac = int(input("\nAdet: "))

            for i in range(isimkac):
                rasgele_isim = random.choice(isimler).strip()
                print(f": {rasgele_isim}")
        else:
            print("Dosya boş veya okunamıyor.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def get_external_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"\nLocal IP: {local_ip}")

        external_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        print(f"Public IP: {external_ip}")

    except Exception as e:
        print(f"Hata: {e}")

def ping():
    isping = input("URL: ")
    
    try:
        ping1 = requests.post(isping)
        ping1.raise_for_status() 
        
        if ping1.status_code == 200:
            print("Başarılı bir şekilde bağlantı kuruldu.")
        else:
            print(f"Bağlantı kuruldu, ancak yanıt kodu: {ping1.status_code}")

    except Exception as e:
        print(f"Hata: {e}. İletişim kurulamadı, internet bağlantınızı kontrol ediniz.")

def hava():
    sehir = input("\nŞehir: ")
    url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + "76758c1245c6bb9bcd6265ac89f63333" + "&q=" + sehir

    veri = requests.get(url)
    verijson = veri.json()

    if verijson["cod"] != "404":
        temp = verijson["main"]["temp"] - 273.15  
        description = verijson["weather"][0]["description"]
        pressure = verijson["main"]["pressure"]
        country = verijson["sys"]["country"]

        print(f"\nSıcaklık: {temp:.2f} °C")  
        print("Açıklama: " + description)
        print("Basınç: " + str(pressure))
        print("Ülke: ", country)
    else:
        print("Şehir bulunamadı.")

def pwd():
 dizin = os.getcwd()
 print(dizin)

def cd():
    try:
        dizin_yolu = input("Dizin yolu: ")
        os.chdir(dizin_yolu)
        print(f"Dizin değiştirildi. Yeni dizin: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Hata: {dizin_yolu} dizini bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def yazitura():
    print("Para atılıyor...")
    time.sleep(1)
    
    y_t = ("Yazı", "Tura")
    
    return print(random.choice(y_t))

def touch():

    dosya_adi = input("Dosya adı: ")

    try:
        with open(dosya_adi, "x") as dosya:
            print(f"{dosya_adi} adlı dosya oluşturuldu.")
    except FileExistsError:
        print(f"{dosya_adi} adlı dosya zaten var.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def df():

    print("\nÇıkmak için <>")

    while True:
        data = input("Veri: ")
        index = input("Index: ")

        if data == "<>" or index == "<>":
            break
        series = pd.Series(data, index=[index])

        with open("data.txt", "a") as file:
            file.write(series.to_string() + '\n')

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

def crypto():
 try:
  urlsorgu = input("Birim: ").upper()
 
 #BTC
  url = f"https://www.google.com/finance/quote/BTC-{urlsorgu}?hl=tr"

  sayfa = requests.get(url)

  html = BeautifulSoup(sayfa.content, "html.parser")

  btc = html.find("div",class_="YMlKec fxKbKc").getText()
 

 #ETH
  url1 = f"https://www.google.com/finance/quote/ETH-{urlsorgu}?hl=tr"

  sayfa1 = requests.get(url1)

  html1 = BeautifulSoup(sayfa1.content, "html.parser")

  eth = html1.find("div",class_="YMlKec fxKbKc").getText()
 


 #DOG
  url2 = f"https://www.google.com/finance/quote/DOGE-{urlsorgu}?hl=tr"

  sayfa2 = requests.get(url2)

  html2 = BeautifulSoup(sayfa2.content, "html.parser")

  dogecoin = html2.find("div",class_="YMlKec fxKbKc").getText()
 
  print(f"""
BTC/{urlsorgu} {btc}
ETH/{urlsorgu} {eth}
DOGECOIN/{urlsorgu} {dogecoin}
""")

 except Exception as ex:
  print(f"Bir hata oluştu {ex}")

def maintest(size_byte):
 i = int(math.floor(math.log(size_byte, 1024)))
 power = math.pow(1024, i)
 size = round(size_byte / power, 2)
 return f"{size} Mbps"

def sptest():
 
 wifi = speedtest.Speedtest()
 print("\nDownload hızı ölçülüyor...")
 download_speed = wifi.download()

 print("\nUpload hızı ölçülüyor...")
 upload_speed = wifi.upload()

 print("\nDownload:", maintest(download_speed))
 print("Upload:", maintest(upload_speed))

def pomodoro():
    sure_dakika = 25  
    sure_saniye = sure_dakika * 60
    print(f"Pomodoro başladı! Süre: {sure_dakika} dakika")

    time.sleep(sure_saniye)

    print("\nSüre doldu! Dinlenmeniz için 5 dakika.")
    dinlenme_sure = 5 * 60
    time.sleep(dinlenme_sure)
    print("\nDinlenme süresi doldu.")

def trash():
 pwdsorgu = input("Dizin yolu: ")
 dosyadi = input("Dosya adı: ")

 dosya_yolu = os.path.join(pwdsorgu, dosyadi)

 os.remove(dosya_yolu) 
def du():
    try:
        directory_path = input("Dizin: ")

        def get_directory_size(directory_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            return total_size

        def format_size(size_in_bytes):
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_in_bytes < 1024.0:
                    return "{:.2f} {}".format(size_in_bytes, unit)
                size_in_bytes /= 1024.0
            # Büyük boyutlar için döngüden çıkıldığında bir değer döndür
            return "{:.2f} TB".format(size_in_bytes)

        directory_size = get_directory_size(directory_path)

        print("\nDizin Boyutu:", format_size(directory_size))

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def ls():
    dosya_listesi = os.listdir()
    for dosya in dosya_listesi:
        renk = Fore.GREEN if dosya.startswith('.') else Style.RESET_ALL
        print(renk + dosya)

def borsa():
 url = f"https://www.google.com/finance/quote/GARAN:IST?hl=tr"

 sayfa = requests.get(url)

 html = BeautifulSoup(sayfa.content, "html.parser")

 garanti = html.find("div",class_="YMlKec fxKbKc").getText()
 



 url = f"https://www.google.com/finance/quote/AKBNK:IST?hl=tr"

 sayfa = requests.get(url)

 html = BeautifulSoup(sayfa.content, "html.parser")

 akbnk = html.find("div",class_="YMlKec fxKbKc").getText()
 print(f"""\n
AKBNK {akbnk}
GARAN {garanti}
""")

def supercalc():
    while True:
        print("""
İşlemi seçin:
1. Türev
2. İntegral
3. Karekök
4. Cosinus
5. Sinüs
6. Çıkış
""")

        choice = input("Seçiminizi yapın (1-6): ")

        if choice == '6':
            print("Programdan çıkılıyor...")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            num = float(input("Bir sayı veya ifade girin: "))
            x = sp.symbols('x')

            if choice == '1':
                result = sp.diff(num, x)
                print("Türev: {}".format(result))
            elif choice == '2':
                result = sp.integrate(num, x)
                print("İntegral: {}".format(result))
            elif choice == '3':
                result = sp.sqrt(num)
                print("Karekök: {}".format(result))
            elif choice == '4':
                result = sp.cos(num)
                print("Cosinus: {}".format(result))
            elif choice == '5':
                result = sp.sin(num)
                print("Sinüs: {}".format(result))
        else:
            print("Geçersiz giriş. Lütfen 1-6 arasında bir seçenek girin.")

def mp3():
    try:
        path = input("\nDosya yolu: ")

        if path:
            pygame.mixer.init()
            pygame.mixer.music.load(path)  
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  

            pygame.mixer.quit()  
            print("\nMüzik tamamlandı.")

        else:
            print("\nDosya yolu girilmedi.")  
    except Exception as e:
        print(f"Bir şeyler ters gitti! {e}")

def radio():
 main = input("Radyo URL girin: ").strip().lower()

 player = vlc.MediaPlayer(main)
 player.play()

 while True:
    user_input = input("\nÇıkmak için 'q': \n").strip().lower()
    if user_input == 'q':
        break

 player.stop()

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

def clean():
    cwd = input("Yol: ")

    try:
        for dosya_adi in os.listdir(cwd):
            dosya_yolu = os.path.join(cwd, dosya_adi)
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)
            elif os.path.isdir(dosya_yolu):
                os.rmdir(dosya_yolu)

        print("\nÇalışma dizini temizlendi.")
    except Exception as hata:
        print(f"\nHata: {hata}")

def rainbow():
    colors = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫️","⚪️","🟤"]

    for i in range(900000):
        randm = random.choice(colors)
        print(randm)

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

def control():
 keyboard = Controller()
 while True:
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    network_usage /= 1024 
    ram_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent(interval=3)
    if cpu_usage >= 85:
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
        print(f"CPU {cpu_usage}%")
    
    if ram_usage >= 65:
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        print(f"RAM {ram_usage}%")
    
    if cpu_usage >= 90 and ram_usage >= 85:
       print("System reboot")
       time.sleep(7)
       os.system("reboot")
    time.sleep(0.5)

def change_keyboard_layout(layout_name):
    ctypes.windll.user32.LoadKeyboardLayoutW(layout_name, 1)

def slot():
    sembol = ["🍒", "🍓"]
    nesne = []

    for i in range(3):
        choc = random.choice(sembol)
        nesne.append(choc)

    if nesne[0] == nesne[1] == nesne[2]:
        print(*nesne, sep=' ')
        print("\n\033[0;32mKAZANDINIZ!\n\033[0m")
        if len(sembol) > 2:
            sembol.pop(2)
        if len(sembol) > 1:
            sembol.pop(1)
        if len(sembol) > 0:
            sembol.pop(0)
    else:
        print(*nesne, sep=' ')
        print("\n\033[0;31mKAYBETTİNİZ!\n\033[0m")

def find():
    bulunan_dosyalar = []
    dizin = input("Dizin: ")
    uzanti = input("Uzantı: ")

    dosya_listesi = os.listdir(dizin)
    
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(dizin, dosya_adi)
        
        if os.path.isfile(dosya_yolu) and dosya_adi.endswith(uzanti):
            bulunan_dosyalar.append(dosya_yolu)
     
    if bulunan_dosyalar:
     for dosya in bulunan_dosyalar:
        print(f"\n{dosya}")
    else:
      print(f"{uzanti} uzantılı dosya bulunamadı.")

def mac():
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        print(f"MAC Adresi: {mac}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def searchduck():
 print("Çıkış için: 'q'")
 while True:
     search = input("\nDuckDuckGo: ")
     if search == "q":
        break
     url = f"https://duckduckgo.com/?hps=1&q={search}&ia=web"
     webbrowser.open(url)

def searchgoogle():
 print("Çıkış için: 'q'")
 while True:
     search = input("\nGoogle: ")
     if search == "q":
        break
     url = f"https://www.google.com/search?q={search}&sca_esv=7e63893fda4bafb0&sca_upv=1&sxsrf=ACQVn09uW9n4DHl6Gv--82QMIoeJuCek_A%3A1712412524611&ei=bFcRZqfuJPSGxc8Pgu2F2As&udm=&ved=0ahUKEwin1PPh4a2FAxV0Q_EDHYJ2AbsQ4dUDCBA&uact=5&oq=sela&gs_lp=Egxnd3Mtd2l6LXNlcnAiBHNlbGEyChAuGEMYgAQYigUyCxAuGIAEGLEDGIMBMggQLhiABBixAzIIEC4YgAQYsQMyCBAuGLEDGIAEMgsQLhiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyGRAuGEMYgAQYigUYlwUY3AQY3gQY3wTYAQNI1BNQ8ANY1wpwAngAkAEAmAG5AaAB3gWqAQMwLjW4AQPIAQD4AQGYAgegAroGqAISwgINEC4YQxiABBiKBRiwA8ICDhAAGIAEGIoFGLEDGLADwgINEAAYgAQYigUYQxiwA8ICCxAAGIAEGLEDGLADwgIIEAAYgAQYsAPCAgoQIxiABBiKBRgnwgIEECMYJ8ICChAAGIAEGIoFGEPCAgUQABiABMICChAuGIAEGIoFGEPCAgcQIxjqAhgnwgITEAAYgAQYigUYQxjqAhi0AtgBAcICFhAuGEMYgAQYigUYyAMY6gIYtALYAQLCAhwQLhiABBiKBRhDGMcBGNEDGMgDGOoCGLQC2AECwgIQEC4YgAQYigUYQxixAxiDAcICBRAuGIAEwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiABBiKBRixAxiDAZgDEIgGAZAGCroGBggBEAEYAboGBggCEAEYCLoGBggDEAEYFJIHBTIuNC4xoAf1YQ&sclient=gws-wiz-serp"
     webbrowser.open(url)

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

def domain_checker():
    try:
        domain = input("Domain: ")
        
        domain_info = whois.whois(domain)

        # WHOIS bilgilerini ekrana yazdır
        print("Domain Bilgileri:")
        print(f"Domain Adı: {domain_info.domain_name}")
        print(f"Oluşturulma Tarihi: {domain_info.creation_date}")
        print(f"Son Güncelleme Tarihi: {domain_info.last_updated}")
        print(f"Bitiş Tarihi: {domain_info.expiration_date}")

        if domain_info.status:
            print("Durumlar:")
            for status in domain_info.status:
                print(f"  - {status}")

    except whois.parser.PywhoisError as e:
        print(f"Hata: {e}")

def mouse():
    print("Testi sonlandırmak için: 'Ctrl + C'")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Fare pozisyonu: X={x}, Y={y}")

            time.sleep(1)  # Her saniye kontrol et

    except KeyboardInterrupt:
        print("\nTesti sonlandırdınız.")

def saving():
    try:
     dkinput = int(input("Dakika: "))
     print(f"\n{Fore.RED}Tasarruf moduna geçildi, sistem {dkinput} dakika sonra kapanacak.")
     print("\nÇıkmak için: 'Ctrl + c'")
     dk = dkinput 
     saniye = dk * 60
     time.sleep(saniye)
     os.system("shutdown")
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")

def gsm():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    number = int(input("Adet: "))
    
    for _ in range(number):
        gsm_data = "05"
        
        for _ in range(9):  # 8 haneli rastgele numara ekleme
            digit = random.choice(data)
            gsm_data += str(digit)
        
        print(Fore.GREEN + f"{gsm_data}" + Fore.RESET)

def evrim():
 nfor = int(input("Adet: "))
 url = "https://evrimagaci.org/ufukderin2001/rss.xml"
 feed = feedparser.parse(url)

 for i, entry in enumerate(feed.entries[:nfor], 1):
                if 'description' in entry:
                    haber_basligi = BeautifulSoup(entry.description, 'html.parser').get_text()
                    print(f"\n{i}. {haber_basligi}\n\033[36m{entry.link}\n\033[0m")
                else:
                    print(f"\n{i}. Haber başlığı alınamadı.\n\033[36m{entry.link}\n\033[0m")

def upgr():
    print(os.system("sudo apt upgrade"))

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

def position():
    while True:
     url = "https://www.google.com/search?q="
     start_x, start_y = pyautogui.position()

     current_x, current_y = pyautogui.position()

     if current_x != start_x or current_y != start_y:
        webbrowser.open(url)
        break

def numcheck():
    Key = "6d6f969fd9024ac8afde957f0c86a5ba"
    number = input("GSM: ")

    check_number = phonenumbers.parse(number)

    number_location = pn_geocoder.description_for_number(check_number, "en")
    print(number_location)

    service = carrier.name_for_number(check_number, "en")
    print(service)

    geocoder_api = OpenCageGeocode(Key)  
    query = str(number_location)
    results = geocoder_api.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Konum", lat, lng)

def genaii():
 try:
  genai.configure(api_key="AIzaSyDWoJAFMI-t5tBYZOpz9cE4AXPFOR4OSQ4")
  
  generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

  safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

  convo = model.start_chat(history=[
])
  print("\nÇıkış için 'q'")
  while True:
   send = input("\n\nAI: ")
   if send == "q":
    break
   convo.send_message(send)
   print(f"\n{convo.last.text}")
 except Exception as e:                                                                                                           
  print(e)

print(f"""
\n\n\nBu uygulama BETA sürümündedir, bazı şeyler değişebilir veya bozulabilir.\n\n

{Fore.RED}███████╗██╗   ██╗ ██████╗ ██╗    ██╗   ██╗███████╗ █████╗  █████╗ 
{Fore.RED}██╔════╝██║   ██║██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗██╔══██╗
{Fore.RED}█████╗  ██║   ██║██║   ██║██║    ██║   ██║█████╗  ╚██████║╚█████╔╝
{Fore.WHITE}██╔══╝  ╚██╗ ██╔╝██║   ██║██║    ╚██╗ ██╔╝██╔══╝   ╚═══██║██╔══██╗
{Fore.WHITE}███████╗ ╚████╔╝ ╚██████╔╝███████╗╚████╔╝ ███████╗ █████╔╝╚█████╔╝
{Fore.WHITE}╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝ ╚════╝  ╚════╝ 
                                                        Version BETA 2.1.4                

""")

time.sleep(1.8)



isletim_sistemi = platform.system()

if isletim_sistemi == "Windows":
        os.system("cls")

elif isletim_sistemi in ["Linux", "Darwin"]:
    os.system("clear")
    
print("\nKomutlar: 'help'")

while True:
    dizin = os.getcwd()
    if admin:
        main = input("\033[30mAdmin:\033[0m ").strip().lower()

    if reset == True:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.WHITE} ").strip().lower()

    if red == True:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.RED} ").strip().lower()

    if blue == True:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.BLUE} ").strip().lower()

    if yellow == True:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.YELLOW} ").strip().lower()

    if green == True:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.GREEN} ").strip().lower()     

    if not admin and not red and not reset and not yellow and not blue and not green:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.WHITE} ").strip().lower()
    
    if main not in [
        "",
        "help", 
        "userinfo",
        "sysinfo",
        "date",
        "calc",
        "temp",
        "shut",
        "note",
        "notebook",
        "fx",
        "nick",
        "cls",
        "pass",
        "ip",
        "qrcode",
        "ping",
        "weather",
        "pwd",
        "cd",
        "fp",
        "touch",
        "web",
        "crypto",
        "mail",
        "speedtest",
        "shutdown",
        "reboot",
        "trash",
        "pomodoro",
        "ls",
        "du",
        "stock",
        "scalc",
        "mp3",
        "data",
        "coal",
        "admin",
        "radio",
        "radiolist",
        "news",
        "clean",
        "rainbow",
        "twt",
        "twthelp",
        "todo",
        "afad",
        "en",
        "slot",
        "find",
        "search",
        "shop",
        "domain",
        "saving",
        "mouse",
        "gsm",
        "bilim",
        "rulet",
        "machange",
        "control",
        "ascii",
        "version",
        "youtb",
        "cal",
        "upd",
        "upg",
        "red","blue","green","yellow","reset",
        "onion",
        "posi",
        "numcheck",
        "ai",
        "btext"
        ]:

     print(f"\n{Fore.RED}Bilinmeyen Komut{Fore.RESET}")

    if main == "help":
        help()

    if main == "date":
        print(f"\nTarih: {tarih_str}")

    if main == "calc":
        calculator()

    if main == "sysinfo":
         sysinfo()    

    if main == "temp":
        get_temperatures()

    if main == "shut":
        print("\nUygulama kapatıldı.")
        break

    if main == "note":
        note()
        

    if main == "notebook":
      notebook()

    if main == "fx":
        doviz()


    if main == "web":
         web()    

    if main == "cls":
       clear()
      

    if main == "pass":
        generate_password()

    if main == "qrcode":
       qrcodde()

    if main == "nick":
        isim_sec()

    if main == "ip":
     get_external_ip()

    if main == "ping":
         ping()     
         
    if main == "weather":
        hava()
    
    if main == "pwd":
        pwd()
    
    if main == "cd":
        cd()
    
    if main == "fp":
        yazitura()
    
    if main == "touch":
        touch()

    if main == "crypto":
        crypto()

    if main == "mail":
        mail()

    if main == "speedtest":
        sptest()
    
    if main == "reboot":
        reboot()
    
    if main == "shutdown":
        kapat()
    
    if main == "trash":
        trash()

    if main == "ls":
       ls()

    if main == "du":
        du()
    
    if main == "stock":
       borsa()

    if main == "scalc":
        supercalc()

    if main == "mp3":
        mp3()
    
    if main == "data":
        df()
    
    if main == "coal":
        maden()

    if main == "admin":
      admin = True
    
    if main == "radio":
       radio()
    
    if main == "radiolist":
       radiolist()
    
    if main == "news":
       news()
    
    if main == "clean":
       clean()
    
    if main == "rainbow":
       rainbow()

    
    if main == "twthelp":
       twitterhelp()
    
    if main == "twt":
       twt()

    if main == "todo":
       task()
    
    if main == "afad":
       afad()
    
    if main == "en":
       change_keyboard_layout("00000409")
    
    if main == "slot":
      slot()
       
    if main == "find":
       find()
    
    if main == "mac":
       mac()
    
    if main == "search":
       print("""
1) DuckDuckGo
2) Google
""")
       choice = input("\nMotor: ")
       if choice == "1":
           os.system("clear")
           searchduck()

       if choice == "2":
           os.system("clear")
           searchgoogle()

    if main == "shop":
       shop()
    
    if main == "domain":
        domain_checker()
    
    if main == "pomodoro":
        pomodoro()
    
    if main == "saving":
        saving()
    
    if main == "mouse":
        mouse()
    
    if main == "gsm":
        gsm()
    
    if main == "bilim":
        evrim()
    
    if main == "rulet":
        rulet()
    
    if main == "machange":
        Machange()
    
    if main == "control":
        control()
    
    if main == "ascii":
        video_path = input("Video: ")
        video_to_ascii(video_path)
    
    if main == "version":
        print("\nBeta v2.1.4")

    if main == "youtb":
        youtb()
    
    if main == "cal":
        caleda()
    
    if main == "upd":
        upd()
    
    if main == "upg":
        upgr()
    
    if main == "red":
        red = True
        blue = False
        yellow = False
        green = False
        reset = False

    if main == "reset":
        reset = True
        red = False
        blue = False
        yellow = False
        green = False
    
    if main == "blue":
        reset = False
        red = False
        blue = True
        yellow = False
        green = False
    
    if main == "yellow":
        reset = False
        red = False
        blue = False
        yellow = True
        green = False
    
    if main == "green":
        reset = False
        red = False
        blue = False
        yellow = False
        green = True
    
    if main == "onion":
        onion()
    
    if main == "posi":
        position()
    
    if main == "numcheck":
        numcheck()
    
    if main == "ai":
        genaii()

    if main=="btext":
        btext()