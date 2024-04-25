import time
def pomodoro():
    sure_dakika = 25  
    sure_saniye = sure_dakika * 60
    print(f"Pomodoro başladı! Süre: {sure_dakika} dakika")

    time.sleep(sure_saniye)

    print("\nSüre doldu! Dinlenmeniz için 5 dakika.")
    dinlenme_sure = 5 * 60
    time.sleep(dinlenme_sure)
    print("\nDinlenme süresi doldu.")
