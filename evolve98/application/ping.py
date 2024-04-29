import requests
def ping():
    isping = input("URL: ")
    
    try:
        ping1 = requests.post(isping)
        ping1.raise_for_status() 
        
        if ping1.status_code == 200:
            print("bağlantı kuruldu.")
        else:
            print(f"Bağlantı kuruldu, ancak yanıt kodu: {ping1.status_code}")

    except Exception as e:
        print(f"Hata: {e}. İletişim kurulamadı, internet bağlantınızı kontrol ediniz.")
