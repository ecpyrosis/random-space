#!/usr/bin/env python

user_input = input('What is your phrase? ')
phrase = (user_input.replace('of', '').replace('without', 'with out').split())
# print(phrase)
acro = ""
for i in phrase:
    acro = acro + i[0].upper()
print('From the phrase:  {}'.format(user_input))
print('We converted it like so: {}'.format(phrase))
print('Your acronym is: {}'.format(acro))
