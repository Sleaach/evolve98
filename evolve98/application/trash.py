import os
def trash():
 pwdsorgu = input("Dizin yolu: ")
 dosyadi = input("Dosya adı: ")

 dosya_yolu = os.path.join(pwdsorgu, dosyadi)

 os.remove(dosya_yolu) 