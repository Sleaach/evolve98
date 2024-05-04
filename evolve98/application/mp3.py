import pygame
def mp3():
    try:
        path = input("\nDosya yolu: ")

        if path:
            pygame.mixer.init()
            pygame.mixer.music.load(path)  
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  

            pygame.mixer.quit()  
            print("\nMüzik tamamlandı.")

        else:
            print("\nDosya yolu girilmedi.")  
    except Exception as e:
        print(f"Bir şeyler ters gitti! {e}")
