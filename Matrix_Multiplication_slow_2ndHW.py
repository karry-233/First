#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:40:37 2018

@author: karry
"""


""" n * n Matrix multiplication (slow version)"""


import numpy, sys, time


if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n)) # Matrix A
b = numpy.zeros((n, n)) # Matrix B
c = numpy.zeros((n, n)) # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0

begin = time.time()

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i, j] += a[i, k] * b[k, j]

end = time.time()
print("time: %.6f sec" % (end - begin))


# Print C for debugging. Comment out the print before measuring the execution time.
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
total = 0
for i in range(n):
    #print(c)
    for j in c[i]:
        #print(j)
        total = total + j 
        
print("sum: %.6f" % total)

