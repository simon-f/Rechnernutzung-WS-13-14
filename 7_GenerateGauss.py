#!/usr/bin/python -tt
import numpy as np
import matplotlib.pyplot as plt
 
#generate some Gaussion distributed Data and save to file


data_x = np.random.normal(loc=1.5, scale= 0.5, size=100)
data_y = np.random.normal(loc=0.6, scale= 0.15, size=100)  
  
data_r = np.divide(data_x, data_y)

np.savetxt('r.dat',data_r)

