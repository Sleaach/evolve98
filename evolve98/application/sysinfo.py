import psutil
from colorama import Fore,Style
import platform
def sysinfo():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    net_info = psutil.net_io_counters()
    operating_system = platform.system()
    cpuinfo = platform.processor()
    print("\nSistem Bilgileri:")
    print(f"İşletim sistemi: {operating_system}")
    print(f"CPU Mimarisi: {cpuinfo}")
    print(f"CPU Kullanımı: {Fore.GREEN}{cpu_percent}%{Style.RESET_ALL}")
    print(f"RAM Kullanımı: {Fore.BLUE}{ram_percent}%{Style.RESET_ALL}")
    print(f"Disk Kullanımı: {Fore.MAGENTA}{disk_percent}%{Style.RESET_ALL}")
    print(f"İşlemci Sayısı: {psutil.cpu_count(logical=False)} (Fiziksel)")
    print(f"Toplam Bellek: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Aktif Ağ Bağlantıları: {net_info.packets_sent} gönderilen, {net_info.packets_recv} alınan")
