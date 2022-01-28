#!/usr/bin/env python

word1 = 'apples'
word2 = 'oranges'

def commonLetter(a):
    if a in word1 and a in word2:
        print("Common Letters: " + a )
    else:
        print("There are no common Letters")

commonLetter('a')
commonLetter('g')

def inBoth(word1, word2):
    for i in word1:
        if i in word2:
            print(i)

inBoth('apples', 'oranges')







