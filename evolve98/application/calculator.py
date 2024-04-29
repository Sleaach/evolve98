def calculator():
    while True:
        print("\nişlem seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")

        secim = input(": ")

        if secim == "5":
             break

        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")
            continue

        if secim == "1":
            sonuc = sayi1 + sayi2
        elif secim == "2":
            sonuc = sayi1 - sayi2
        elif secim == "3":
            sonuc = sayi1 * sayi2
        elif secim == "4":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                print("Hata: Sıfıra bölme hatası.")
                continue
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue

        print(f"Sonuç: {sonuc}")
