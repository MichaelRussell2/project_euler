import math
import numpy as np

def is_prime(n):
    for i in xrange(2,n):
        if n % i == 0:
            return False
        elif i > math.sqrt(n):
            break
        else:
            continue
    return True

i=1
primes = []
while True:
    i+=1
    if is_prime(i):
        primes.append(i)
    elif len(primes) >= 10001:
        break
    else:
        continue

print primes[-1]    
