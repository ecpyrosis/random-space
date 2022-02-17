#! /usr/bin/env python

wordlist = [item for item in input("Enter a word to see if it is a palindrome): ").split()]
print(wordlist)

def ispalindrome(i):

    reversedList = wordlist[::-1]

    # reversedList = [forwardList[::-1] for forwardlist in words]
    # if reversedList == forwardlist:
    #     return(wordlist + " is a palindrome")
    # else:
    #     return(wordlist + " is not palindrome")
    if reversedList == wordlist:
        return("that is a palindrome")
    else:
        return("sorry that is not palindrome")

print(ispalindrome(wordlist))



