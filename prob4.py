#! user/bin/python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools

def backwards(n): #finds reverse of a number
    s = str(n)
    l = len(s)
    backward = []
    for i in range(l):
        backward.append(s[l-i-1])
    return "".join(backward)

def palindromic(n): #tests for palindromes
    if str(n) == str(backwards(n)):
        return True
    else:
        return False

palindromes = [] #finds palindromes with two 3-digit factors
for n, m in itertools.product(range(100, 1000), range(100, 1000)): #for elements in Cartesian product
    if palindromic(n * m) == True:
        palindromes.append(n * m)

print max(palindromes)

                

        


