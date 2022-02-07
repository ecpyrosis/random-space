#! /usr/bin/python

# make a string of n length with n characters
# to simulate a unix diretory
# https://unix.stackexchange.com/questions/367008/why-is-socket-path-length-limited-to-a-hundred-chars


from random import choice
from string import ascii_lowercase

def makestring(n):
    string_val = "".join(choice(ascii_lowercase) for i in range(n))
    dir_val = "/".join(string_val[i:i+5] for i in range(0, len(string_val), 5))
    return dir_val

print(makestring(104))
print(makestring(105))