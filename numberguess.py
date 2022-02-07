#!/usr/bin/env python

from random import randint

number = randint(1,50)
tries = 0
input("Guess a number between 1 - 50:\n")

def guess(number):
    tries += 1
    if input == number:
        print("Correct! You took " + tries + "guesses to get it right!" )
        exit()
    elif input < number:
        print("Getting cold...")
    elif input > number:
        print("Too hot...")

guess(input)
