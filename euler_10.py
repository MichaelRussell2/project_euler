#!/usr/bin/env python

import math

def is_prime(n):
    
    if n < 2:
        return False
    for i in xrange(2,n):
        if n % i == 0:
            return False
        elif i > math.sqrt(n):
            break
        else:
            continue
    return True

primes = 0
stop=2000000
for i in xrange(stop):
    print i
    if is_prime(i): primes += i

print primes
