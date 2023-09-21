import random

print("Vítej v casinu!")

MONEY = 10000
print(f"Tvůj aktuální obnos peněz: {MONEY}")

while MONEY > 0:
    
    BET_MONEY = int(input("Kolik si přeješ vsadit? "))

    COLOR = (input("Na jakou barvu chceš vsadit? "))

    numer = random.randint(1, 37)
    if numer == 37:
        color = "zelená"
        
    else:
        if numer % 2 == 1:
            color = "červená"

        elif numer % 2 == 0:
            color = "černá"
            
    print(f"Barva na kterou to padlo je: {color}.")
        
    if numer == 37:
        print("Zelená není šťasná barva:(")
        MONEY -= MONEY

    elif color == COLOR:
        print(f"Gratuluju, vyhrál jsi: {BET_MONEY}!")
        MONEY += BET_MONEY
    else:
        print(f"Ajaj, prohrál jsi: {BET_MONEY}.")
        MONEY -= BET_MONEY

    if MONEY <= 0:
        print("Bohužel jsi prohrál. Hra končí!")
    else:
        print(f"Konec hry. Tvé peníze: {MONEY}")
