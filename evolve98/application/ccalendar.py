from colorama import Fore
import calendar as c

def caleda():
    y = int(input("Yıl: "))
    m = int(input("Ay: "))
    print(f"\n,{Fore.GREEN}{c.month(y,m)}")
