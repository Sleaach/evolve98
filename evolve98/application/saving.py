import time
from colorama import Fore
import os
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
