def touch():

    dosya_adi = input("Dosya adı: ")

    try:
        with open(dosya_adi, "x") as dosya:
            print(f"{dosya_adi} adlı dosya oluşturuldu.")
    except FileExistsError:
        print(f"{dosya_adi} adlı dosya zaten var.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
