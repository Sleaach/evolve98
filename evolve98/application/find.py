import os
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
