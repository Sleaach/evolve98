import os
def clean():
    cwd = input("Yol: ")

    try:
        for dosya_adi in os.listdir(cwd):
            dosya_yolu = os.path.join(cwd, dosya_adi)
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)
            elif os.path.isdir(dosya_yolu):
                os.rmdir(dosya_yolu)

        print("\nÇalışma dizini temizlendi.")
    except Exception as hata:
        print(f"\nHata: {hata}")
