# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:07:25 2015

@author: smudd
"""

def CRN_model_plotting():
    
    ########################
    #
    # Read the data
    #
    ########################
    DataDirectory = "C://basin_data//Model_results//"
    FileName = "CRNvariable_padova_1_0_0.er_frame_metadata"
    
    FileName = DataDirectory+FileName
    f = open(FileName,'r')  # open file
    lines = f.readlines()   # read in the data
    f.close()               # close the file
    
    n_lines = len(lines)   # get the number of lines (=number of data)  
    
    