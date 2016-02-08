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

def step_change(lambda1, lambda2,eold,A,t_vec):
    
    #top_time_vec1 = np.exp( np.multiply(t_vec,(eros/Gamma+lambda2)))
    #bottom_time_vec1 = np.exp( np.multiply(t_vec,(eros/Gamma+lambda1)))
    
    #print top_time_vec1
    #print bottom_time_vec1 
    
    #top_term1 = np.add(1,np.multiply(np.add(top_time_vec1,-1),np.exp(dbr/Gamma)))
    
    #print "tt1:"
    #print top_term1
    
    ratios = []

    for t in t_vec:
        top_term1 = Gamma*(eold-A*eold)*lambda1+A*np.exp(t*(A*eold/Gamma+lambda1))*eold*(eold+Gamma*lambda1)
        top_term2 = A*eold-eold+(eold+Gamma*lambda2)*np.exp(t*(A*eold/Gamma+lambda2))
        
        bottom_term1 = Gamma*(eold-A*eold)*lambda2+A*np.exp(t*(A*eold/Gamma+lambda2))*eold*(eold+Gamma*lambda2)
        bottom_term2 = A*eold-eold+(eold+Gamma*lambda1)*np.exp(t*(A*eold/Gamma+lambda1))        
        
        #print t
        #print top_term1
        #print top_term2
        #print ratio
        
        ratio = (top_term1*top_term2)/(bottom_term1*bottom_term2)
        
        ratios.append(ratio)
        #print t
        #print top_term1
        #print ratio
        

    #print ratios
    return ratios
    
def step_change_plot(lambda1,lambda2,t_vec):

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
    ax1.fill_between(ky_times,1,1.2,facecolor = 'gray')
    #,linewidth = 1,)
   
    eros1 = 0.0026
    eros2 = 0.026 
    A1 = 2
    A2 = 5
    ratios1 = step_change(lambda1, lambda2,eros1,A1,t_vec)
    ratios2 = step_change(lambda1, lambda2,eros1,A2,t_vec)
    
    ratios3 = step_change(lambda1, lambda2,eros2,A1,t_vec)
    ratios4 = step_change(lambda1, lambda2,eros2,A2,t_vec)


    ax1.plot(ky_times,ratios1,'k-',linewidth = 2) 
    ax1.plot(ky_times,ratios2,'k:',linewidth = 2) 
    ax1.plot(ky_times,ratios3,'b--',linewidth = 2)  
    ax1.plot(ky_times,ratios4,'b-.',linewidth = 2)             

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
    #ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_ylim([1,2.5])
    ax1.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
            
    plt.ylabel('Ratio', fontsize = label_size)
    plt.xlabel('Time since erosion rate change (kyr)', fontsize = label_size) 

    #===========================================
    # And now the second subplot
    #===========================================
    ax2 = Fig1.add_subplot(gs[5:100, 57:97])    

    # plot the 1:1 line
    #print ky_times.size
    #print zero_vec.size
    #print tw_percent.size
    ax2.fill_between(ky_times,0.8,1,facecolor = 'gray')
    #,linewidth = 1,)

    eros1 = 0.0026
    eros2 = 0.026 
    A1 = 0.2
    A2 = 0.5
    ratios1 = step_change(lambda1, lambda2,eros1,A1,t_vec)
    ratios2 = step_change(lambda1, lambda2,eros1,A2,t_vec)
    
    ratios3 = step_change(lambda1, lambda2,eros2,A1,t_vec)
    ratios4 = step_change(lambda1, lambda2,eros2,A2,t_vec)


    ax2.plot(ky_times,ratios1,'k-',linewidth = 2) 
    ax2.plot(ky_times,ratios2,'k:',linewidth = 2) 
    ax2.plot(ky_times,ratios3,'b--',linewidth = 2)  
    ax2.plot(ky_times,ratios4,'b-.',linewidth = 2)           

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
    #ax2.set_yscale('log')
    ax2.set_xscale('log')
    ax2.set_ylim([0.2,1])
    ax2.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
            
    plt.ylabel('Ratio', fontsize = label_size)
    plt.xlabel('Time since erosion rate change (kyr)', fontsize = label_size)

    #plt.show()       
    Fileformat = "svg"
    plt.savefig("Erate_change.svg",format = Fileformat)
    plt.show()    

if __name__ == "__main__":
    lambda1 = 121.0*(10**-6)
    lambda2 = 500*(10**-9)
    Gamma = 160.0
    log_t_vec = np.linspace(2.0,6.0,1000)
    t_vec = np.power(10,log_t_vec)

    t = np.asarray(t_vec)
    step_change_plot(lambda1,lambda2,t)      
       
    