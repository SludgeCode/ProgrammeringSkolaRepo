import random
number: int = random.randint(1,10)
print("gissa ett tal mellan 1 och 10")
round = 0
while round > 3:
    guess: int = input(f"Försök {round}: gissa talet: ")
    if guess == number:
        print("Rätt gissat")
        round = 4
    else:
        print("Fel gissat.")
        round += 1