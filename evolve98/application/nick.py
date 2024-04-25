import random
def nick():
    try:
        with open("nick.txt", "r", encoding="utf-8") as dosya:
            isimler = dosya.readlines()

        if isimler:
            isimkac = int(input("\nAdet: "))

            for i in range(isimkac):
                rasgele_isim = random.choice(isimler).strip()
                print(f": {rasgele_isim}")
        else:
            print("Dosya boş veya okunamıyor.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
