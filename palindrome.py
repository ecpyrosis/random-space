#! /usr/bin/env python

words = input("Enter a word to see if it is a palindrome): \n")

def ispalindrome(words):
    forwardlist = words
    reversedList = forwardlist[::-1]
    # reversedList = [forwardList[::-1] for forwardlist in words]
    if reversedList == forwardlist:
        return(words + " is a palindrome")
    else:
        return(words + " is not palindrome")

print(ispalindrome(words))



