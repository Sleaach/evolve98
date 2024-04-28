import math
import sympy as sp
def supercalc():
    while True:
        print("""
İşlemi seçin:
1. Türev
2. İntegral
3. Karekök
4. Cosinus
5. Sinüs
6. Çıkış
""")

        choice = input("Seçiminizi yapın (1-6): ")

        if choice == '6':
            print("Programdan çıkılıyor...")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            num = float(input("Bir sayı veya ifade girin: "))
            x = sp.symbols('x')

            if choice == '1':
                result = sp.diff(num, x)
                print("Türev: {}".format(result))
            elif choice == '2':
                result = sp.integrate(num, x)
                print("İntegral: {}".format(result))
            elif choice == '3':
                result = sp.sqrt(num)
                print("Karekök: {}".format(result))
            elif choice == '4':
                result = sp.cos(num)
                print("Cosinus: {}".format(result))
            elif choice == '5':
                result = sp.sin(num)
                print("Sinüs: {}".format(result))
        else:
            print("Geçersiz giriş. Lütfen 1-6 arasında bir seçenek girin.")
