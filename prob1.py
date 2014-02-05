#!/usr/bin/python

""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
multiples = []

def mult_sum(n):
    for a in range(n):
        if a % 3 == 0 or a % 5 == 0:
            print a
            multiples.append(a)


    print "Multiples of 3 or 5 less than " + str(n) + "are: " + str(multiples)
    print "Their sum is: " + str(sum(multiples))

mult_sum(1000)



