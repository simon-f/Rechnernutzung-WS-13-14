#!/usr/bin/env python
#     (the first line allows execution directly from the linux shell) 
#
# --- sinmple python exercise 
# Author:        G. Quast   Oct. 2013
# dependencies:  PYTHON v2.7, numpy
# last modified: 
#--------------------------------------------------------------
import numpy as np
import math # used for floor function
import operator

# write here your own implementation of the stistical funcions

def mean(a):
  return np.sum(a) / len(a)

def variance(a):
  mean_value = mean(a)
  return np.sum([(n-mean_value)**2 for n in a]) / len(a)

def sigma(a):
  return np.sqrt(variance(a))

# --- main program
#
# read data from text file
a = np.loadtxt('numbers.dat',dtype=float)
N = len(a)
print N, " numbers read \n", a

#     print same statistical quantities using numpy functions
print "\n*==* result with numpy functions:"
print "median is:",np.median(a)
print "mean is",np.mean(a)
print "variance is",np.var(a) 
print "standard deviation sigma=",np.std(a)
print "unbiased sigma =",np.std(a)*np.sqrt(float(N)/float(N-1))

 
# ---> your code starts here ....
print "\n\n---- own implementations -----\n"

# calculate and print some statistical quantities on raw data

print "\n---- Aufgabe a.) ----"
print "mean:\t\t", mean(a)
print "variance:\t", variance(a)
print "sigma:\t\t", sigma(a)

# histogram data
print "\n---- Aufgabe b.) ----"
occurence = [0] * 10
for i in xrange(0, N):
  occurence[int(a[i])] += 1
print "occurences:\t", occurence

# calculate mean and sigma from histogram and print
print "\n---- Aufgabe c.) ----"

mean2  = sum(map(operator.mul, occurence, range(0,10))) / float(len(a))
sigma2 = np.sqrt(sum(map(operator.mul, occurence, [(i - mean2)**2 for i in range(0,10)])) / float(len(a)))

print "mean:\t\t", mean2
print "sigma:\t\t", sigma2
