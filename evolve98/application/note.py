
def note():
    with open("note.txt", "a") as note:
            while True:
                notebook_entry = input("(Çıkmak için exit) Notebook: ")
                if notebook_entry == "exit":
                    print("\nNotebook uygulamasından çıkış yapıldı.")
                    break
                note.write(f"\n{notebook_entry}")
         
