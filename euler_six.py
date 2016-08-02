import math
import numpy as np

def diff(max):
    sumsq = sum([x**2 for x in xrange(1,max+1)])
    sqsum = (sum([x for x in xrange(1,max+1)]))**2
    return sqsum - sumsq


print diff(100)
