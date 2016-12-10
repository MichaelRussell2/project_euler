#!/usr/bin/env python

def triplet(target):
    for i in range(1, target):
        for j in range(i, target):
            if i+j > target: continue 
            for k in range(j, target):
                if i*i +j*j == k*k and i + k + j == target:
                    return i*j*k

print triplet(1000)                
