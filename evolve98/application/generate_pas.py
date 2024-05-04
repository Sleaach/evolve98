import string
import random
def generate_password():
    while True:
        try:
            hane = int(input("Hane: "))
            if hane > 0:
                break
            else:
                print("Lütfen pozitif bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    sifre = ""
    haneler = string.ascii_letters + string.digits + string.punctuation

    for i in range(hane):
        sifrecc = random.choice(haneler)
        sifre += sifrecc

    print(f"Oluşturulan şifre: {sifre}")