#!/usr/bin/python

"""What is the 10001st prime number?"""

def prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

primes = {}
count = 0
for n in range(2, 9999999):
    if prime(n) == True:
        count += 1
        print  str(n) + " is the " + str(count) + "th prime" 
        primes[n] = count
        if primes[n] == 10001:
            print str(n) + " is the one!"
            break
        

