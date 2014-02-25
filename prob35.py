#!/usr/bin/python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import itertools

def sieve(n): # Sieve of Eratosthenes algorithm
    np1 = n + 1 
    s = list(range(np1)) 
    s[1] = 0 
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i)) 
    return filter(None, s)


def rotations(n):
    """
    Find all rotations (cyclic permutations) of the digits of n.

    We do this by iterating over all the indices into the digits of n,
    splitting the string into two halves, and swapping the order of
    the halves.

    For example, when 12345 gets split at index 2:

    rhs = '345'
    lhs = '12'

    rhs + lhs = '34512'
    """
    digits = str(n)
    rotations = []
    for i in range(len(digits)):
        rhs = digits[i:]
        lhs = digits[:i]
        rotations.append(int(rhs + lhs))
    return rotations

def combinations(n):
    combo_lst = []
    for permutation in itertools.permutations(str(n), len(str(n))):
        concatenation = ""
        for m in permutation:
            concatenation = concatenation + m
        concatenation_int = int(concatenation)
        combo_lst.append(concatenation_int)
    return combo_lst

def circular_primes(k): # returns list of circular primes less than k
    circular_primes_less_than_k = []
    lst = list(sieve(k))
    for n in lst:
        for m in set(rotations(n)):
            if m not in lst:
                break
        else:
            circular_primes_less_than_k.append(n)
    return circular_primes_less_than_k

print circular_primes(1000000)


