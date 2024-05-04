import os
try:
 def changename():
    oldfile=input("File: ")
    newfile=input("New Name: ")
    gg = os.rename(oldfile,newfile)
    print("New file name: ",gg)
except Exception as e:
  print(e)
