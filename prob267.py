#!/usr/bin/python
#  coding=utf-8


"""
You are given a unique investment opportunity.

Starting with 1 of capital, you can choose a fixed proportion, f, of your capital to bet on a fair coin toss repeatedly for 1000 tosses.

Your return is double your bet for heads and you lose your bet for tails.

For example, if f = 1/4, for the first toss you bet 0.25, and if heads comes up you win 0.5 and so then have 1.5. You then bet 0.375 and if the second toss is tails, you have 1.125.

Choosing f to maximize your chances of having at least 1,000,000,000 after 1,000 flips, what is the chance that you become a billionaire?

All computations are assumed to be exact (no rounding), but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.
"""


"""
There are two tasks. Task A is to find the value of f which will maximize the chances of yielding 1,000,000,000 after 1,000 flips. Task B is to give the probability of becoing a billionaire for that f.

Let p(n) be the amount of money in the pot at stage n.
Let f be in range(0,1)

The pot increments as follows:

When n = 0, p(n) = 1

At stage n, p(n) = p(n-1) + f*p(n-1) if heads
                   p(n-1) -f*p(n-1) if tails

The quickest way to reach 1,000,000,000 is if f = 1 and we get heads every time.Then, we get 1,000,000,000 after log_2(1,000,000,000) = 29.897 tosses. Of course, setting f = 1 makes big losses equally likely too. There is a 50% chance that the game will be over after the first coin toss.
                   
"""

the_pot = [1]
# a list of how much money is in the pot at each stage.


#The number of times we´ve tossed a coin is n-1, where n is the length of the list.

f = 1
#This is the chosen value of f

print "the coin has been flipped " + str(len(the_pot)-1) + " times." 


while len(the_pot) <=1000:

    if coin_toss == heads:
        append.the_pot((1+f) * the_pot[(len(the_pot)])

    if coin_toss == tails:
        append.the_pot((1-f) * the_pot[(len(the_pot)])


"""

def p(n):
    if n == 0:
        p(n) = 1
    elif coin_toss == heads:
            p(n) = (1+f) * p(n-1)
            the_pot.append(p(n))
    elif coin_toss == tails:
            p(n) = (1-f) * p(n-1)
            the_pot.append(p(n))


for n in range(1,1000):
    p(n)

"""

print the_pot
