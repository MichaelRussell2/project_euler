#!/usr/bin/env python

with open('11.dat') as f:
    data = f.read().splitlines()

M=[i.split() for i in data]
N=[[int(j) for j in i] for i in M]

maxN = 0

#up-down and left-right
for i in xrange(len(N)):
    for j in xrange(len(N)-3):

        hor = N[i][j]*N[i][j+1]*N[i][j+2]*N[i][j+3]
        if hor > maxN: maxN = hor

        ver = N[j][i]*N[j+1][i]*N[j+2][i]*N[j+3][i]
        if ver > maxN: maxN = ver

#diagonal            
for i in xrange(len(N)-3):
    for j in xrange(len(N)-3):

        diag1 = N[i][j]*N[i+1][j+1]*N[i+2][j+2]*N[i+3][j+3]
        if diag1 > maxN: maxN = diag1

        diag2 = N[i][j+3]*N[i+1][j+2]*N[i+2][j+1]*N[i+3][j]
        if diag2 > maxN: maxN = diag2

print maxN
