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
from glob import glob

def CRN_model_timeseries(dirname):
 
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
    #DataDirectory = "C://basin_data//Model_results//June2015_results//HighK//ER_metadata//"
    #FilePrefix = "CRNVF_long_HighK_0_0_1var"
    #FileName = FilePrefix+".er_frame_metadata"
    

    for FileName in glob(dirname+"CRNVF_long_HighK_*.er_frame_metadata"): # assigns a number to each iteration (i.e. for every .tree file in the directory)

      # clear the figure
      pp.clf()      
      
      print "Filename is: " + FileName

      split_fname = FileName.split('\\')
      no_tree_levs = len(split_fname) 
      this_fname = split_fname[no_tree_levs-1]
      print "fname: "+FileName+" and this fname: "+this_fname
        
      FilePrefix = this_fname.split('.')[0]

    
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
      #leg = pp.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
      #       ncol=3, mode="expand", borderaxespad=0.)
      

      pp.rcParams['xtick.direction'] = 'in'
      pp.rcParams['ytick.direction'] = 'in'
      #ax1.set_xscale('log')
      #ax1.set_yscale('log')
       
      if "1_0_0" in FilePrefix:
          ax1.set_ylim(0,0.4)
      else:
          ax1.set_ylim(0.1,0.3)
          
      ax1.set_xlim(200,500)
  
  
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
      pp.title(FilePrefix)
      
      # make the labels fit
      fig.subplots_adjust(bottom=0.2) 
      fig.subplots_adjust(left=0.2) 
      
      #fig.tight()
      #pp.ylim(0,1)

      #set the file format
      fformat = 'svg'      

      figname = FilePrefix+"_erosion_v2."
      figname = figname+fformat
      pp.savefig(figname, format=fformat)  
   
        
if __name__ == "__main__":
    DataDirectory = "C://basin_data//Model_results//June2015_results//HighK//ER_metadata//"    
    CRN_model_timeseries(DataDirectory)         
        