# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:22:49 2016

@author: fedel_000
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

Path = r"C:\Users\fedel_000\Documents\Measurements\stefano\03_10_Angle_resolved_Fluorescence_TMPyP_HClpH1_AuNC_05mWatt\ASCII"
#Path = r"C:\Users\fedel_000\Documents\Measurements\stefano\02_25_Angle_resolved_Raman_TMPyP_HClpH1_AuNC\ASCII"
#Path = r"C:\Users\fedel_000\Documents\Measurements\stefano\03_15_Raman_Fluorescence_focus\ASCII"
s = '\\'
files = os.listdir(Path)

nSigma = 2

for j in range(5):
    path = Path + s + files[j]
    print j
    df = pd.read_csv(path, sep=',', header=None).astype(float)
    df = df.transpose()
    
    fig1 = plt.figure( figsize = (20, 10))
    ax1 = fig1.add_subplot(311)
    ax2 = fig1.add_subplot(312)
    ax3 = fig1.add_subplot(313)
    spectrum = []
    Max = []
    #N_pixel = 100
    for N_pixel in range(len(df) - 2 ):
        n_pixel = 100
        bg = df.ix[:n_pixel][N_pixel].mean()
        #df.ix[:n_pixel][N_pixel] = df.ix[:n_pixel][N_pixel] - bg
        RMS = ( np.sum( ( df.ix[:n_pixel][N_pixel] - bg )**2  ) / n_pixel )**0.5
        index = np.where(df.ix[:][N_pixel] > bg + nSigma *RMS)
        #print index
        
        df.ix[: ][N_pixel] = df.ix[ index[0] ][N_pixel] - bg
        spectrum = spectrum + [ df.ix[ index[0] ][N_pixel].sum() ]# index[0] is the set of all the data that are bigger then the chosen thresold
        ax2.plot( df.ix[1:][N_pixel] )
        Max = Max + [ np.max(spectrum) ]
        #plt.draw()
        #plt.pause(0.4)
    
    
    #plt.figure( figsize =(20, 10))
    MAX = np.max(Max)
    line1, = ax1.plot(spectrum)
    ax1.set_ylim(0, MAX)
    ax1.set_xlim(0, 510)
    ax3.imshow(df, cmap=cm.gray)
    #plt.draw()
    

    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.imshow(df, cmap=cm.gray)
    #plt.grid()