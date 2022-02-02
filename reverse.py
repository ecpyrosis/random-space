#!/usr/bin/env python

# def reverse_string(word):
#     for i in word[::-1]:
#         print(i)
# reverse_string('pooch')


# def reverse_string(word):
#     r = word[::-1]
#     print(r)

def reverse_string(word):
     print(word[::-1])

reverse_string("Here's an example")
reverse_string('pooch')

# uh, these seem to be identical, do not need to use split()
def reverse_words_in_sentence(sentence):
    # sentence.split()
    print(sentence[::-1])

reverse_words_in_sentence("here is a sentence")

