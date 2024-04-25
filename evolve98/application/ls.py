import os
from colorama import Style,Fore
def ls():
    dosya_listesi = os.listdir()
    for dosya in dosya_listesi:
        renk = Fore.GREEN if dosya.startswith('.') else Style.RESET_ALL
        print(renk + dosya)
