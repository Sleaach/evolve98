import os
def reboot():
    try:
        os.system("reboot now")  
    except Exception as e:
        print(f"\nSistem yeniden başlatma hatası: {e}\n")