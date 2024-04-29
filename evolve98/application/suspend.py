import os
op = os.name
def susp():
    if op == 'nt':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif op == 'posix':
        os.system("sudo systemctl suspend")
    else:
        print("Bu işletim sistemi desteklenmiyor.")

