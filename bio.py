#!/usr/env python

import time

bio = []

def getName():
    name = input('What is your name? ')
    try:
        name == name.isalpha()
        bio.append(name)

    except ValueError:
        print('That is not a name!')
 
def getBirth():
    birth = input('What is your date of birth? (MM/DD/YY) ')
    try:
        birth == time.strptime(birth, '%m/%d/%y')
        bio.append(birth)

    except ValueError:
        print('That is not a date')

def getAddr():
    addr = input('What is your full address? ')
    try:
        addr == addr.isalnum()
        bio.append(addr)
      
    except ValueError:
        print('That is not an address!')

def getGoals():
    goals = input('What are your personal goals? ')
    try:
        goals == goals.isalnum()
        bio.append(goals)
     
    except ValueError:
        print('Not so sure about that....')


getName()
getBirth()
getAddr()
getGoals()


print('Hello ' + bio[0] +'!')
print('Your birthday is ' + bio[1])
print('You live at ' + bio[2])
print("You're goals are " + bio[3])