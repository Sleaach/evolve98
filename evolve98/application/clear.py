import subprocess
import platform
def clear():
    isletim_sistemi = platform.system()

    if isletim_sistemi == "Windows":
        subprocess.call("cls", shell=True)
    elif isletim_sistemi in ["Linux", "Darwin"]:
        subprocess.call("clear", shell=True)
    else:
        print("Bu işletim sistemi desteklenmiyor.")
