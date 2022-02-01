#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Magic_8-ball

from random import randint

answers = [ "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",]

input("Think of your question. When ready, press enter/return")

print(answers[randint(0,19)])

# for i in answers:
#     print(answers.index(i))



