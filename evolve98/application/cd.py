import os
def cd():
    try:
        dizin_yolu = input("Dizin yolu: ")
        os.chdir(dizin_yolu)
        print(f"Dizin değiştirildi. Yeni dizin: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Hata: {dizin_yolu} dizini bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
