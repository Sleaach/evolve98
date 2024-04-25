def task():
    tasks = []   

    while True:
        print("""
1. Görev Ekle
2. Görev Sil
3. Görev Görüntüle
4. Çıkış
        """)
        choice = input(": ")

        if choice == "1":
            while True:
                tass = input("Görev: ")
                if tass.lower() == "4":
                    break
                else:
                    tasks.append(tass) 

        if choice == "2":
            print("Silmek istediğin görevi yaz.")
            while True:
                delet = input("\nGörev: ")
                if delet.lower() == "4":
                    break
                try:
                    tasks.remove(delet)
                    print(f"Görev '{delet}' silindi.")
                except ValueError:
                    print(f"Görev '{delet}' bulunamadı. Lütfen tekrar deneyin.")

        if choice == "3":
            print("Görevler:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        if choice == "4":
           break
