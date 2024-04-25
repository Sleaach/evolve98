import random
def slot():
    sembol = ["🍒", "🍓"]
    nesne = []

    for i in range(3):
        choc = random.choice(sembol)
        nesne.append(choc)

    if nesne[0] == nesne[1] == nesne[2]:
        print(*nesne, sep=' ')
        print("\n\033[0;32mKAZANDINIZ!\n\033[0m")
        if len(sembol) > 2:
            sembol.pop(2)
        if len(sembol) > 1:
            sembol.pop(1)
        if len(sembol) > 0:
            sembol.pop(0)
    else:
        print(*nesne, sep=' ')
        print("\n\033[0;31mKAYBETTİNİZ!\n\033[0m")
