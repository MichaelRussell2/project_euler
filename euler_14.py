import math
import numpy as np

def next(n):
    if (n % 2 == 0):
        return n/2
    else:
        return 3*n+1

def len_sequence(start):
    alist=[]    
    alist.append(start)
    i=0
    while True:
        if alist[i] == 1:
            break
        alist.append(next(alist[i]))
        i+=1
    return len(alist)
        
stop_iter = 1000000
ks = np.zeros(stop_iter)
for k in xrange(1,stop_iter):
    ks[k] = len_sequence(k)
    
print np.max(ks), np.argmax(ks)
