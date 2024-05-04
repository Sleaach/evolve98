from colorama import Fore
import random
import time
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