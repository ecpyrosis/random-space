#!/usr/bin/env python

import random

number = random.randint(1,50)
print(number)
guess = int(input("Guess a number between 1 and 50: "))
tries = 0
while guess != number:
    if guess < number:
        tries += 1
        print("Too cold. Try again")
        guess = int(input("Guess a number between 1 and 50: "))
    else:
        tries += 1
        print("Too hot. Try again")
        guess = int(input("Guess a number between 1 and 50: "))

tries += 1
print("You guessed correctly! It took you " + str(tries) + " tries" )





