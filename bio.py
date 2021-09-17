#!/usr/bin/env python

import time

bio = []

name = input('What is your name? ')
print(name)
if name.isalpha():
    bio.append(name)
else:
    print('That is not a name!')
 
birth = input('What is your date of birth? (MM/DD/YY) ')
if time.strptime(birth, '%m/%d/%y'):
    bio.append(birth)
else:
    print('That is not a date')

addr = input('What is your full address? ')
bio.append(addr)
# if addr.isalnum():
#     bio.append(addr)
# else:
#     print('That is not an address!')

goals = input('What are your personal goals? ')
# if goals.isalnum():
bio.append(goals)
# else:
#     print('Not so sure about that....')


print('Hello ' + bio[0] +'!')
print('Your birthday is ' + bio[1])
print('You live at ' + bio[2])
print("You're goals are " + bio[3])