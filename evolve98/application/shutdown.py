import os
def kapat():
    osy = os.name
    try:
        if osy == "Linux":
         os.system("shutdown now")
        else:
            os.system("shutdown /s /f /t 0")  
    except Exception as e:
        print(f"\nSistem kapatma hatası: {e}\n")
