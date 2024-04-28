import pyautogui
import webbrowser
def position():
    while True:
     url = "https://www.google.com/search?q="
     start_x, start_y = pyautogui.position()

     current_x, current_y = pyautogui.position()

     if current_x != start_x or current_y != start_y:
        webbrowser.open(url)
        break
