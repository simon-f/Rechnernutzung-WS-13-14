#####################################################
# Aufgabe 5: Fermifunktion
#

import numpy as np
import matplotlib.pyplot as plt

# fermi function
def fermi_dirac(e, t, kb=1, mu=0):
    return 1.0 / (np.exp( (e-mu) / (kb*t) ) + 1)

# temperatures
temperatures = [0.1, 0.5, 1, 2, 5]

# calculate sampling points 
n_points = 256
e_min, e_max = -10, 10
E = np.linspace(e_min, e_max, n_points, endpoint =  True)

# define colors 
colors = ["red", "green", "blue", "black", "orange"] 

# plot functions for multiple values of t using the colors specified in the color array
for idx, t in enumerate(temperatures):
    F = [fermi_dirac(e,t) for e in E]
    plt.plot(E, F, color=colors[idx - (len(colors)- 1)], label=r'$T='+str(t)+'$')

# place ticks
plt.xticks(np.linspace(e_min,e_max,5,endpoint=True))
plt.yticks(np.linspace(0,1,5,endpoint=True))

# set axis delimiters 
plt.xlim(e_min, e_max)
plt.ylim(-0.05, 1.05)

# show grid
plt.grid(True)

# place legend
plt.legend(loc='lower left')

# print everything on screen
plt.show();
