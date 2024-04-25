import qrcode
def qrcodde():
    try:
     veri = input("QR Kod oluşturulacak veriyi girin: ")
     dosya_yolu = input("QR Kod dosyasını kaydetmek istediğiniz yolu girin: ").strip().lower()

     if veri:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(veri)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(dosya_yolu)

        print(f"QR kodu oluşturuldu ve '{dosya_yolu}' olarak kaydedildi.")
     else:
        print("QR kodu oluşturulamadı.")
    except Exception as f: 
         print(f"Bir hata oluştu. {f}")
