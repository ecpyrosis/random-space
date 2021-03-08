#!/bin/env python

rounds = 0

while rounds < 3:

    noun = input('Enter a noun\n')
    adj = input('Enter an adjective\n')
    adv = input('Enter an adverb\n')
    exl = input('Enter an exclamation\n')

    print(exl + ' ! he said '+ adv + ' as he jumped into his convertable ' + noun + ' and drove off with his '+ adj +      ' wife.')
    rounds += 1