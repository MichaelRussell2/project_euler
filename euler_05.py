import math
import numpy as np

def test(num,denom):
    for i in xrange(1,denom+1):
        if num % i != 0:
            return False
        else:
            continue
    return True

i=0
while True:
    i+=1
    if test(i,20):
        print "%d divides by numbers 1-20" % i
        break
    else:
        continue
    

