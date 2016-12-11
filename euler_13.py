#!/usr/bin/env python

import numpy as np
from sys import stdout

data=np.loadtxt('13.dat',dtype=object)
nums = []

for i in xrange(len(data)):
    nums.append(long(data[i]))

ans = str(sum(nums))

for i in xrange(10):
    stdout.write('%s, ' % ans[i])
stdout.write('\n')    
