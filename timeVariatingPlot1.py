# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 21:21:06 2016

@author: fedel_000
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-3, 3, 0.01)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
j = 0
k = 0
y = []
Time = 0.05

while j < 200:
    y = y + [ (np.sin(np.pi*x*k)  / (np.pi*x*k) )**2 ]
    line, = ax.plot(x, y[j], 'b') # all the plots will be blue
    plt.draw()
    plt.pause(Time)
    print j
    #line.remove()
    j = j + 1
    k = k + 0.01*j

