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

def get_primefactor(i):
    for j in xrange(2,i):
        if i % j == 0 and is_prime(j) :
            print "%d is a prime factor of %d" % (j, i)
        if j > math.sqrt(i):
            break          
    return
    
get_primefactor(600851475143)             
