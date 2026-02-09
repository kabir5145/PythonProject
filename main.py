# Guess the Number Game

import random

a = random.randint(1, 10)   # number between 1 and 10
max_tries = 3               # total allowed attempts
tries = 0

print("Welcome to Guess the Number Game!")
print("Guess a number between 1 and 10")
print("You have only 3 tries")

while tries < max_tries:
    ans = int(input("Enter your guess: "))
    tries += 1   # increase attempt count

    if ans == a:
        print("Correct You won in", tries, "tries!")
        break
    elif ans > a:
        print("Too high ")
    elif ans == a+1:
        print("Little high")
    elif ans == a-1:
        print("Little low")
    else:
        print("Too low ")

else:
    print("Game Over You used all tries!")
    print("The correct number was:", a)


