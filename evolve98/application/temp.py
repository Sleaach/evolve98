import psutil
from colorama import Fore,Style
def get_temperatures():
    try:
        temp_info = psutil.sensors_temperatures()

        if 'coretemp' in temp_info:
            cpu_temp = temp_info['coretemp'][0].current
            print(f"CPU Sıcaklığı: {Fore.RED}{cpu_temp}°C{Style.RESET_ALL}")

        if 'radeon' in temp_info:
            gpu_temp = temp_info['radeon'][0].current
            print(f"GPU Sıcaklığı: {Fore.YELLOW}{gpu_temp}°C{Style.RESET_ALL}")

        if 'acpitz' in temp_info:
            other_temp = temp_info['acpitz'][0].current
            print(f"Diğer Bileşen Sıcaklığı: {Fore.CYAN}{other_temp}°C{Style.RESET_ALL}")

    except Exception as e:
        print(f"Sıcaklık okuma hatası: {e}")
