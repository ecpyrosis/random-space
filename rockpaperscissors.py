#!/usr/bin/env python

# lets code some rock, paper, scissors!
import random

# what shit code, update to use a dict
# myItems = {'1':'rock', '2':'paper', '3':'scissors'}
# for i in myItems.values():
#     print(i)

play1 = int(input("Choose:\n 1) Rock 2) Paper 3) Scissors\n"))

if play1 == 1:
    myPlay = "rock"
elif play1 == 2:
    myPlay = "paper"
elif play1 == 3:
    myPlay = "scissors"
else:
    print("That makes no snese")

play2 = random.randint(1,3)
if play2 == 1:
    yourPlay = "rock"
elif play2 == 2:
    yourPlay = "paper"
elif play2 == 3:
    yourPlay = "scissors"

if play1 == play2:
    print("We both picked " + myPlay.swapcase() + " Its a tie!")
elif play1 > play2:
    print(myPlay.swapcase() + " beats " + yourPlay.swapcase() + " You win!")
else:
    print(yourPlay.swapcase() + " beats " + myPlay.swapcase() + " You lose!")



