import random
number: int = random.randint(1,10)
guess: int = input("gissa ett tal mellan 1 och 10: ")
if number == guess:
    print("!du hade rätt!")
else:
    print(f"Tyvärr, det var {number}")