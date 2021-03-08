#!/usr/bin/env python

# odd or even

cont = 'yes'
while (cont == 'yes' or cont == 'y'):

    print('Give a number between 1 and 1000, and I will tell you if it is even or odd')
    num = input('What number are you thinking?\nInput: ')

    try:
        numIn = int(num)
        if (numIn < 1 or numIn > 1000):
            print('That is not a number between 1 and 1000, bye!')
            break

        elif numIn % 2 == 0:
            print("That's an even number!")
            a = input('Have another?')
            if (a == 'yes' or a == 'y'):
                continue 
            else:
                print('ok bye')
                break
        else:
            print("That's an odd number!")
            a = input('Have another?')
            if (a == 'yes' or a =='y'):
                continue 
            else:
                print('ok bye')
                break
    except(TypeError):
        numIn == (num)
        print('That is not a number', numIn)
