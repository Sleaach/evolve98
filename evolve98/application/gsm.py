import random
from colorama import Fore
def gsm():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    number = int(input("Adet: "))
    
    for _ in range(number):
        gsm_data = "05"
        
        for _ in range(9):
            digit = random.choice(data)
            gsm_data += str(digit)
        
        print(Fore.GREEN + f"{gsm_data}" + Fore.RESET)
