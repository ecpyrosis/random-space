#!/usr/bin/env python

# def reverse_string(word):
#     for i in word[::-1]:
#         print(i)
# reverse_string('pooch')


# def reverse_string(word):
#     r = word[::-1]
#     print(r)

# print(str(new_string))

# print(reverse_string("Here's an example"))
# print(reverse_string('pooch'))

# def reverse_words_in_sentence(sentence):
#     sentence.split()
#     for i in (sentence[::-1]):
#         print(i)

# mystring = "Santa Cruz is cool"
# new_string = mystring.split()
# list.reverse(new_string)
# print(new_string)

# Python code to Reverse each word
# of a Sentence individually

# Function to Reverse words
# def reverseWordSentence(Sentence):
#     # Splitting the Sentence into list of words.
#     words = Sentence.split(" ")
#
#     # Reversing each word and creating
#     # a new list of words
#     # List Comprehension Technique
#     newWords = [word[::-1] for word in words]
#
#     # Joining the new list of words
#     # to for a new Sentence
#     newSentence = " ".join(newWords)
#
#     return newSentence

# reverse a string
def reverse_string(word):
    return(word[::-1])

# reverse words in a sentence
def reverse_words_in_sentence(sentence):
    words = sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence


print(reverse_string("Here's") == "s'ereH")
print(reverse_words_in_sentence("This is an example"))

# simple way to test
print(reverse_words_in_sentence("This is an example") == "sihT si na elpmaxe")
print(reverse_words_in_sentence("Here's another sentence") == "s'ereH rehtona ecnetnes")

