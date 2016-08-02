import math
import numpy as np

def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

a=[]
i=0

while True:
    j=fibonacci(i)
    if (j <= 4000000) and (j % 2 == 0):
        print j
        a.append(j)
    elif ( j > 4000000):
        break
    i+=1
    
print np.sum(a)                
        
