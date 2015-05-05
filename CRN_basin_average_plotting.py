# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:07:25 2015

@author: smudd
"""

import matplotlib.pyplot as pp
import numpy as np
from matplotlib import rcParams
import matplotlib.lines as mpllines
from matplotlib.ticker import FormatStrFormatter

def CRN_model_plotting():
 
    # These set the font size
    label_size = 20
    #title_size = 30
    axis_size = 28

    rcParams['font.size'] = label_size
   
    ########################
    #
    # Read the data
    #
    ########################
    DataDirectory = "C://basin_data//Model_results//"
    FilePrefix = "CRNvariable_short_0_0_1var"
    FileName = FilePrefix+".er_frame_metadata"
    
    
    FileName = DataDirectory+FileName
    
    print "Filename is: " + FileName
    
    f = open(FileName,'r')  # open file
    lines = f.readlines()   # read in the data
    f.close()               # close the file
    
    n_lines = len(lines)   # get the number of lines (=number of data)  
    
    # get the data by splitting the data strings
    # first we discard the first line
    DataLines = lines[2:]
    
    #print DataLines
    
    
    # initiate the variables
    D = np.zeros(n_lines-2)
    K = np.zeros(n_lines-2)
    T = np.zeros(n_lines-2)
    E = np.zeros(n_lines-2)
    U = np.zeros(n_lines-2)
    Eapp = np.zeros(n_lines-2)
    
    # loop through the file populating the data vectors
    i = 0
    for line in DataLines:
        splitline = line.split("\t")
        #print splitline
        D[i] = float(splitline[3])
        K[i] = float(splitline[2])
        T[i] = float(splitline[1])/1000     # in kyr
        E[i] = float(splitline[4])*1000     # in mm/yr
        U[i] = float(splitline[5])*1000     # in mm/yr
        Eapp[i] = float(splitline[6])*1000     # in mm/yr
        i= i+1
    
    #print T
    #print U
    #print E
    
    print "mean e is: " + str(E.mean())
    print "mean Eapp is: " + str(Eapp.mean())
    
    # now plot the results    
    fig = pp.figure(1, facecolor='white',figsize=(10,7.5))
    ax1 = fig.add_subplot(1,1,1)  
    
    pp.plot(T,E,linewidth=3,label = ("Erosion rate, $mm/yr$"))
    pp.plot(T,U,linewidth=3,label = ("Uplift rate, $mm/yr$"))
    pp.plot(T,Eapp,linewidth=3,label = ("Apparent erosion rate, $mm/yr$"))
    #pp.legend(loc=2)
    leg = pp.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)

    pp.rcParams['xtick.direction'] = 'in'
    pp.rcParams['ytick.direction'] = 'in'
    #ax1.set_xscale('log')
    #ax1.set_yscale('log')
       
  
  
    ax1.spines['top'].set_linewidth(2.5)
    ax1.spines['left'].set_linewidth(2.5)
    ax1.spines['right'].set_linewidth(2.5)
    ax1.spines['bottom'].set_linewidth(2.5) 
    ax1.tick_params(axis='both', width=2.5)    
    #ax1.xaxis.set_major_formatter(FormatStrFormatter('%.03f'))

    for line in ax1.get_xticklines():
        line.set_marker(mpllines.TICKUP)

    for line in ax1.get_yticklines():
        line.set_marker(mpllines.TICKRIGHT)

    ax1.set_xlabel('Time ($kyr$)',fontsize = axis_size)
    ax1.set_ylabel('Uplift and erosion rates $mm/yr$)',fontsize = axis_size) 
    #pp.title("$A$ is "+str(A)+ " $m^2/g$")
    #pp.ylim(0,1)
    ax1.set_xlim(200,300)

    figname = FilePrefix+"_erosion.svg"
    pp.savefig(figname, format='svg')  


    fig2 = pp.figure(1, facecolor='white',figsize=(10,7.5))
    ax2 = fig.add_subplot(2,1,1)  
    
    ax2.plot(T,D,linewidth=3,label = ("D, $m^2/yr$"))
    
    ax3 = ax2.twinx()    
    
    ax3.plot(T,K,linewidth=3,label = ("K, $variable units$"))
    #ax2.plot(T,U,linewidth=3,label = ("Apparent erosion rate, $mm/yr$"))
    pp.legend(loc=2)

    pp.rcParams['xtick.direction'] = 'in'
    pp.rcParams['ytick.direction'] = 'in'
    #ax1.set_xscale('log')
    #ax1.set_yscale('log')
  
  
    ax2.spines['top'].set_linewidth(2.5)
    ax2.spines['left'].set_linewidth(2.5)
    ax2.spines['right'].set_linewidth(2.5)
    ax2.spines['bottom'].set_linewidth(2.5) 
    ax2.tick_params(axis='both', width=2.5)    
    #ax1.xaxis.set_major_formatter(FormatStrFormatter('%.03f'))

    for line in ax2.get_xticklines():
        line.set_marker(mpllines.TICKUP)

    for line in ax2.get_yticklines():
        line.set_marker(mpllines.TICKRIGHT)

    ax2.set_xlabel('Time ($kyr$)',fontsize = axis_size)
    ax2.set_ylabel('D $m^2/yr$',fontsize = axis_size)
    ax3.set_ylabel('K')
    #pp.title("$A$ is "+str(A)+ " $m^2/g$")
    #pp.ylim(0,1)

    figname = FilePrefix+"_forcing.svg"
    pp.savefig(figname, format='svg')       
        
if __name__ == "__main__":
    CRN_model_plotting()         
        