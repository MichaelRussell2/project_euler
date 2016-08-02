import math
import numpy as np

def is_palindrome(a):
    return str(a) == str(a)[::-1]

pals = []
for i in xrange(100,1000):
    for j in xrange(100,1000):
        if is_palindrome(i*j):
                pals.append(i*j)

print pals[-1]                

