from pynput.keyboard import Key, Controller
import psutil
import time
import os
def control():
 keyboard = Controller()
 while True:
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    network_usage /= 1024 
    ram_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent(interval=3)
    if cpu_usage >= 85:
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
        print(f"CPU {cpu_usage}%")
    
    if ram_usage >= 65:
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        print(f"RAM {ram_usage}%")
    
    if cpu_usage >= 90 and ram_usage >= 85:
       print("System reboot")
       time.sleep(7)
       os.system("reboot")
    time.sleep(0.5)
