import subprocess

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
