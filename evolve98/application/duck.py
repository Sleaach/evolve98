import webbrowser
def searchduck():
 print("Çıkış için: 'q'")
 while True:
     search = input("\nDuckDuckGo: ")
     if search == "q":
        break
     url = f"https://duckduckgo.com/?hps=1&q={search}&ia=web"
     webbrowser.open(url)
