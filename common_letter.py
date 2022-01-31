#!/usr/bin/env python

word1 = 'apples'
word2 = 'oranges'

# function to see if a specific letter matches in 2 strings
def commonLetter(a):
    if a in word1 and a in word2:
        print("Common Letters: " + a )
    else:
        print("There are no common Letters")

commonLetter('a')
commonLetter('g')

# function to find common letters in two strings & print them
def inBoth(word1, word2):
    for i in word1:
        if i in word2:
            print(i)

inBoth('apples', 'oranges')

# function to take a string and write it out backwords

def reverseMe(a):
    for i in a[::-1]:
        print(i)

reverseMe('food')
reverseMe('supercalifragic')


