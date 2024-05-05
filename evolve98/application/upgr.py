import os
def upgr():
 try:
    print(os.system("sudo apt upgrade"))
 except Exception as e:
   print("\n"+e)