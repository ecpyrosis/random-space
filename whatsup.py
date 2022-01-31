#!/usr/bin/env python

count = 0

str1 = (input("What's on your mind today?\n"))

for i in str1.split():
    count += 1

# print(str1.split())

print('That was ' + str(count) + ' words long!\n')


print("Let's read your file now....")
r = open('whatsup.txt')
myText = r.read()
myWords = myText.split()
r.close()

print('Counting words in your file...')
print('wow! that was ' + str(len(myWords)) + ' words long in your file')


