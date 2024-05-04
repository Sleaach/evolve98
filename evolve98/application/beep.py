import winsound
def beep():
    frek = int(input("Frekans: "))
    ms = int(input("Ms: "))
    winsound.Beep(frek, ms)
