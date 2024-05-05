import os
def upd():
    try:
     print(os.system("sudo apt update"))
    except Exception as e:
       print(e)
