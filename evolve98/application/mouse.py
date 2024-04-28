import pyautogui
import time
def mouse():
    print("Testi sonlandırmak için: 'Ctrl + C'")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Fare pozisyonu: X={x}, Y={y}")

            time.sleep(1) 

    except KeyboardInterrupt:
        print("\nTesti sonlandırdınız.")
