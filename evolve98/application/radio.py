import vlc
def radio():
 main = input("Radyo URL girin: ").strip().lower()

 player = vlc.MediaPlayer(main)
 player.play()

 while True:
    user_input = input("\nÇıkmak için 'q': \n").strip().lower()
    if user_input == 'q':
        break

 player.stop()
