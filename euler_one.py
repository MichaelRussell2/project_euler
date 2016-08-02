import math
import numpy as np

a=[]
for i in xrange(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        a.append(i)

print np.sum(a)        
