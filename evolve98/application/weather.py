import requests
def air():
    countrys = input("\nŞehir: ")
    url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + "76758c1245c6bb9bcd6265ac89f63333" + "&q=" + countrys

    data = requests.get(url)
    datajson = data.json()

    if datajson["cod"] != "404":
        temp = datajson["main"]["temp"] - 273.15  
        description = datajson["weather"][0]["description"]
        pressure = datajson["main"]["pressure"]
        country = datajson["sys"]["country"]

        print(f"\nSıcaklık: {temp:.2f} °C")  
        print("Açıklama: " + description)
        print("Basınç: " + str(pressure))
        print("Ülke: ", country)
    else:
        print("Şehir bulunamadı.")
