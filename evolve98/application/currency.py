import requests
def doviz():
    apiurl = "https://v6.exchangerate-api.com/v6/a925a27db978233d2605c41e/latest/USD"

    bozulan = input("Bozulan döviz: ").upper()
    alinan = input("Alınan döviz: ").upper()

    try:
        miktar = float(input(f"Ne kadar {bozulan} bozdurmak istiyorsunuz?: "))
    except ValueError:
        print("Geçerli bir miktar girin. Örneğin: 100.50")
        return  
    sonuc = requests.get(apiurl)
    sonucjs = sonuc.json()

    if sonuc.status_code == 200:
        rates = sonucjs['conversion_rates']

        if alinan in rates and bozulan in rates:
            bozulan_kur = rates[bozulan]
            alinan_kur = rates[alinan]

            alinan_miktar = miktar / bozulan_kur * alinan_kur

            print(f"{miktar} {bozulan} = {alinan_miktar:.2f} {alinan}")
        else:
            print("Geçersiz döviz türü.")
    else:
        print(f"API'den veri alınamadı. Hata kodu: {sonuc.status_code}")
