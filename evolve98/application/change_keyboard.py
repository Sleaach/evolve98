import ctypes

def change_keyboard_layout(layout_name):
    ctypes.windll.user32.LoadKeyboardLayoutW(layout_name, 1)