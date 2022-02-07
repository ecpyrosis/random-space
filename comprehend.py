#!/usr/bin/env python

# play with list comprehensions

# traditional way
#
# # Empty list
# List = []
#
# # Traditional approach of iterating
# for character in 'Geeks 4 Geeks!':
#     List.append(character)
#
# # Display list
# print(List)

# using list comprehension

List = [i for i in 'This is Madness!']
print(List)


# def commonLetter(a):
#     if a in word1 and a in word2:
#         print("Common Letters: " + a )
#     else:
#         print("There are no common Letters")

def commonLetter(a,b):
    return ''.join(set(a).intersection(b))


print(commonLetter("this", "his"))
