import time
import datetime
from colorama import Fore
import platform
import os
from application.btext import *
from application.asci import *
from application.ccalendar import *
from application.machange import * 
from application.task import *
from application.roulette import *
from application.twitter import *
from application.help import *
from application.twitterguild import *
from application.youtube import *
from application.mine import *
from application.shutdown import *
from application.reboot import *
from application.mail import *
from application.clear import *
from application.calculator import *
from application.update import *
from application.sysinfo import *
from application.temp import *
from application.note import *
from application.notepad import *
from application.currency import *
from application.generate_pas import *
from application.qrcode import *
from application.web import *
from application.nick import *
from application.ip import *
from application.ping import *
from application.weather import *
from application.pwd import *
from application.cd import *
from application.flipcoin import *
from application.touch import *
from application.datamanage import *
from application.crypto import *
from application.speedtest import *
from application.pomodoro import *
from application.trash import *
from application.du import *
from application.ls import *
from application.exchange import *
from application.supercalc import *
from application.mp3 import *
from application.radio import *
from application.radio_list import *
from application.news import *
from application.clean import *
from application.rainbow import *
from application.afad import *
from application.control import *
from application.change_keyboard import *
from application.slot import *
from application.find import *
from application.mac import *
from application.duck import *
from application.google import *
from application.shop import *
from application.domain import *
from application.mouse import *
from application.saving import *
from application.gsm import *
from application.evo import *
from application.upgr import *
from application.onion import *
from application.position import *
from application.numcheck import *
from application.ai import *
from application.suspend import *
from application.ytmp3 import *
from application.blackjack import *
from application.dc import *
from application.port import *
from application.spider_net import *
from application.ipcheck import *
from application.renames import *




date = datetime.now()
date_str = date.strftime("%Y-%m-%d %H:%M:%S")
red = False
yellow = False
blue = False
green = False
reset = False
    
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

    if not red and not reset and not yellow and not blue and not green:
     main = input(f"\033[32m{isletim_sistemi}@user{Fore.BLUE}{dizin}\033[0m${Fore.WHITE} ").strip().lower()
    
    if main not in [
        "",
        "help", 
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
        "btext",
        "suspend",
        "ytmp3",
        "blackjack",
        "dc",
        "spider",
        "port",
        "ipch",
        "rename"
        ]:

     print(f"\n{Fore.RED}Bilinmeyen Komut{Fore.RESET}")

    if main == "help":
        help()

    if main == "date":
        print(f"\nTarih: {date_str}")

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
        nick()

    if main == "ip":
     get_external_ip()

    if main == "ping":
         ping()     
         
    if main == "weather":
        air()
    
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
       exchange()

    if main == "scalc":
        supercalc()

    if main == "mp3":
        mp3()
    
    if main == "data":
        df()
    
    if main == "coal":
        mine()

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
       asci()
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
    
    if main=="suspend":
        susp()
    
    if main=="ytmp3":
        ytmp3()
    
    if main == "blackjack":
        blackjack()
    
    if main == "dc":
        dc()
    
    if main == "port":
        scan()
    
    if main == "net":
        net()
    
    if main == "ipch":
        ipch()
    
    if main == "rename":
        changename()