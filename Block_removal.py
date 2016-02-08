# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:47:25 2016

@author: smudd
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FormatStrFormatter

def block_removal(lambda1, lambda2,eros,dbr,t_vec):
    
    #top_time_vec1 = np.exp( np.multiply(t_vec,(eros/Gamma+lambda2)))
    #bottom_time_vec1 = np.exp( np.multiply(t_vec,(eros/Gamma+lambda1)))
    
    #print top_time_vec1
    #print bottom_time_vec1 
    
    #top_term1 = np.add(1,np.multiply(np.add(top_time_vec1,-1),np.exp(dbr/Gamma)))
    
    #print "tt1:"
    #print top_term1
    
    ratios = []

    for t in t_vec:
        top_term1 = 1+np.exp(dbr/Gamma)*(np.exp(t*(eros/Gamma+lambda2))-1)
        top_term2 = (np.exp((dbr+t*eros+t*Gamma*lambda1)/Gamma)*eros)+((np.exp(dbr/Gamma)-1)*Gamma*lambda1)
        
        bottom_term1 = 1+np.exp(dbr/Gamma)*(np.exp(t*(eros/Gamma+lambda1))-1)
        bottom_term2 = (np.exp((dbr+t*eros+t*Gamma*lambda2)/Gamma)*eros)+((np.exp(dbr/Gamma)-1)*Gamma*lambda2)
        
        ratio = (top_term1*top_term2)/(bottom_term1*bottom_term2)
        
        ratios.append(ratio)
        #print t
        #print top_term1
        #print ratio
        

    #print ratios
    return ratios
    
    #top_time_vec2 = np.exp( np.divide(Gamma,np.add( dbr/Gamma,np.multiply(t_vec,(eros+Gamma*lambda1)))))
    #bottom_time_vec2 = np.exp( np.divide(Gamma,np.add( dbr/Gamma,np.multiply(t_vec,(eros+Gamma*lambda2)))))
    
    #print top_time_vec2
    #print bottom_time_vec2 
    
    
def block_removal_plot(lambda1,lambda2,t_vec):

    label_size = 14
    axis_size = 12

    # Set up fonts for plots
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['arial']
    rcParams['font.size'] = label_size
    rcParams['xtick.major.size'] = 1    
    rcParams['ytick.major.size'] = 1    
    
    # make a line for the 20% error
    twenty_percent = [] 
    unity = []
    for t in t_vec:
        twenty_percent.append(1.2)
        unity.append(1)
    tw_percent = np.asarray(twenty_percent)
        
    # get a time scale in kyr
    ky_times = np.divide(t_vec,1000.0)
    #print "ky_times: "    
    #print ky_times
    sz = ky_times.size
    #print sz
    zero_vec = np.zeros(ky_times.size)   
    #print "zero vec: "
    #print zero_vec

    # now make plots based on these data
    # The width in inches (3.14961) is 80 mm.
    Fig1 = plt.figure(1, facecolor='white',figsize=(7.08661,3))  

    # generate a 120,90 grid. 
    gs = GridSpec(100,100,bottom=0.2,left=0.05,right=1.0,top=0.95) 
    ax1 = Fig1.add_subplot(gs[5:100, 5:45])    

    # plot the 1:1 line
    #print ky_times.size
    #print zero_vec.size
    #print tw_percent.size
    ax1.fill_between(ky_times,0.8,1.2,facecolor = 'orange',alpha = 0.3)
    #,linewidth = 1,)

    dbr = 50    
    eros1 = 0.0026    
    ratios1 = block_removal(lambda1, lambda2,eros1,dbr,t_vec)
    eros2 = 0.026
    ratios2 = block_removal(lambda1, lambda2,eros2,dbr,t_vec) 


    ax1.plot(ky_times,ratios1,'k-',linewidth = 2) 
    ax1.plot(ky_times,ratios2,'k--',linewidth = 2)            

    ax1.spines['top'].set_linewidth(2)
    ax1.spines['left'].set_linewidth(2)
    ax1.spines['right'].set_linewidth(2)
    ax1.spines['bottom'].set_linewidth(2) 
    
    # This gets all the ticks, and pads them away from the axis so that the corners don't overlap        
    ax1.tick_params(axis='both', width=1, pad = 1, size=2)
    for tick in ax1.xaxis.get_major_ticks():
            tick.set_pad(2)
            #tick.set_width(3)
    for tick in ax1.yaxis.get_major_ticks():
            tick.set_pad(2)
    
    #for line in ax.yaxis.get_ticklines():
    #    line.set_markersize(25)
    #    line.set_markeredgewidth(3)

        
    # logarithmic axes
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_ylim([0.5,6])
    ax1.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
            
    plt.ylabel('Ratio', fontsize = label_size)
    plt.xlabel('Time since block removal (kyr)', fontsize = label_size) 

    #===========================================
    # And now the second subplot
    #===========================================
    ax2 = Fig1.add_subplot(gs[5:100, 57:97])    

    # plot the 1:1 line
    #print ky_times.size
    #print zero_vec.size
    #print tw_percent.size
    ax2.fill_between(ky_times,0.8,1.2,facecolor = 'orange',alpha = 0.3)
    #,linewidth = 1,)

    dbr = 150    
    eros1 = 0.0026    
    ratios1 = block_removal(lambda1, lambda2,eros1,dbr,t_vec)
    eros2 = 0.026
    ratios2 = block_removal(lambda1, lambda2,eros2,dbr,t_vec) 


    ax2.plot(ky_times,ratios1,'k-',linewidth = 2) 
    ax2.plot(ky_times,ratios2,'k--',linewidth = 2)            

    ax2.spines['top'].set_linewidth(2)
    ax2.spines['left'].set_linewidth(2)
    ax2.spines['right'].set_linewidth(2)
    ax2.spines['bottom'].set_linewidth(2) 
    
    # This gets all the ticks, and pads them away from the axis so that the corners don't overlap        
    ax2.tick_params(axis='both', width=1, pad = 1, size=2)
    for tick in ax2.xaxis.get_major_ticks():
            tick.set_pad(2)
            #tick.set_width(3)
    for tick in ax2.yaxis.get_major_ticks():
            tick.set_pad(2)
    
    #for line in ax.yaxis.get_ticklines():
    #    line.set_markersize(25)
    #    line.set_markeredgewidth(3)

        
    # logarithmic axes
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    ax2.set_ylim([0.5,6])
    ax2.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
            
    plt.ylabel('Ratio', fontsize = label_size)
    plt.xlabel('Time since block removal (kyr)', fontsize = label_size)

    #plt.show()       
    Fileformat = "svg"
    plt.savefig("Step_change.svg",format = Fileformat)
    plt.show()    

if __name__ == "__main__":
    lambda1 = 121.0*(10**-6)
    lambda2 = 500*(10**-9)
    Gamma = 160.0
    #t_vec = [500, 5000]
    
    log_t_vec = np.linspace(2.0,6.0,1000)
    t_vec = np.power(10,log_t_vec)
    #print "Times are: "    
    #print t_vec
    #print "================="
    eros = 0.0026
    dbr = 150.0
    t = np.asarray(t_vec)
    block_removal(lambda1, lambda2,eros,dbr,t)
    block_removal_plot(lambda1,lambda2,t_vec)         
       
    