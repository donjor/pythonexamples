import random

guess = -1
answer = random.randrange(10)

guess = int(input("Guess a Number between 0-10: "))

while answer != guess:
    if guess >= 0 and guess <= 10:
        guess = int(input("Wrong, try again: "))

    elif guess > 10 or guess < 0:
        guess = int(input("Wrong, try a number between 0 - 10: "))

if guess == answer:
    print("Congrats you got the answer correct!!")
