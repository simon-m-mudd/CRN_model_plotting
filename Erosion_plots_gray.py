# -*- coding: utf-8 -*-
"""
Created on Tue May 05 14:08:16 2015

@author: smudd
"""

import numpy as np
import LSDMappingTools as LSDmt
from matplotlib import rcParams

def Erosion_plots(DataDirectory,file_prefix,metadata_prefix,time_slice,variation_flags):
  
    variation_flag_string = str(variation_flags[0])+"_"+str(variation_flags[1])+"_"+str(variation_flags[2])
    MetaFname = metadata_prefix+ variation_flag_string+"var.er_frame_metadata"
    print "Metadata filename is: " + MetaFname
    MetaFname = DataDirectory+MetaFname
    
    # first get the metadata file    
    f = open(MetaFname,'r')  # open file
    lines = f.readlines()   # read in the data
    f.close()               # close the file
    
    n_lines = len(lines)   # get the number of lines (=number of data)  
    
    # get the data by splitting the data strings
    # first we discard the first line
    DataLines = lines[2:]
  
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
      
    # now get the uplift rate at this time slice
    ThisUplift = U[time_slice]
    print "The uplift rate is: " + str(ThisUplift)
    
    # now build the name of the data file
    DataPrefix = file_prefix+str(variation_flags[0])+"_"+str(variation_flags[1])+"_"+str(variation_flags[2])
    DataPrefix = DataPrefix+"var"+str(time_slice)+"_erosion.asc"
    print "The data prefix is: " + DataPrefix
    
    ThisFile = DataDirectory+DataPrefix

    # The colour map is a topic of some debate. Here I have chosen to use a 
    # diverging colourmap since I wanted to show clearly the areas with erosion above 
    # and below the mean. The mean is 0.2 mm/yr. 
    # The seismic colour map has more colour saturation near the mean values
    # so it is a bit easier to see variation in the colours for the variable
    # K and D plots, even though they vary much less than the variable U plots
    tcmap = 'gray'
    clim_label = "Erosion rate in mm/yr"
    
    # This ensures the colouring is centred on the mean value and has the same
    # range across all values. 
    clim_val = (0.0,0.4)
    DensityPlotErosion(ThisFile,tcmap,clim_label,clim_val,ThisUplift)
    #LSDmt.DrapedPlot(ThisFile,DrapeFile)


#==============================================================================
def DensityPlotErosion(FileName, thiscmap='gray',colorbarlabel='Elevation in meters',clim_val = (0,0), uplift_rate = 0):
    
    # extract the relevant filename information  
    
    # note this splitting will depend on the operating system
    # '/' is for Linux and '//' is for windows
    split_fname = FileName.split('//')
    no_tree_levs = len(split_fname) 
    this_fname = split_fname[no_tree_levs-1]  
    FilePrefix = this_fname.split('.')[0]   
    print "FilePrefix is: "+FilePrefix
    
    import matplotlib.pyplot as plt
    import matplotlib.lines as mpllines

    label_size = 20
    #title_size = 30
    axis_size = 28

    # Set up fonts for plots
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['arial']
    rcParams['font.size'] = label_size 

    # get the data
    raster = LSDmt.ReadRasterArrayBlocks(FileName)

    # now get the extent
    extent_raster = LSDmt.GetRasterExtent(FileName)
    
    # first get the data in mm/yr
    raster = np.multiply(raster,1000)    
    
    # now replace the data at rows 0 and nrows-1 with the uplift rate
    raster_shape = raster.shape
    nth_row = raster_shape[0]-1
    print "Raster_shape is: "
    print raster_shape
       
    raster[0,:] = uplift_rate
    raster[nth_row,:]  = uplift_rate
    
    # set the raster extent
    x_min = extent_raster[0]
    x_max = extent_raster[1]
    y_min = extent_raster[2]
    y_max = extent_raster[3]

    # make a figure, sized for a ppt slide
    fig = plt.figure(1, facecolor='white',figsize=(10,7.5))

    # make room for the colorbar
    #fig.subplots_adjust(bottom=0.1)
    #fig.subplots_adjust(top=0.9)
    
    ax1 =  fig.add_subplot(1,1,1)
    im = ax1.imshow(raster, thiscmap, extent = extent_raster)



    # now get the tick marks    
    n_target_tics = 5
    xlocs,ylocs,new_x_labels,new_y_labels = LSDmt.GetTicksForUTM(FileName,x_max,x_min,y_max,y_min,n_target_tics)  
    plt.xticks(xlocs, new_x_labels, rotation=60)  #[1:-1] skips ticks where we have no data
    plt.yticks(ylocs, new_y_labels) 
    
    # some formatting to make some of the ticks point outward    
    for line in ax1.get_xticklines():
        line.set_marker(mpllines.TICKDOWN)
        #line.set_markeredgewidth(3)

    for line in ax1.get_yticklines():
        line.set_marker(mpllines.TICKLEFT)
        #line.set_markeredgewidth(3)  
    
    plt.xlim(x_min,x_max)    
    plt.ylim(y_max,y_min)   
   
    plt.xlabel('Easting (m)',fontsize = axis_size)
    plt.ylabel('Northing (m)', fontsize = axis_size)  

    ax1.set_xlabel("Easting (m)")
    ax1.set_ylabel("Northing (m)")
    
    # set the colour limits
    print "Setting colour limits to "+str(clim_val[0])+" and "+str(clim_val[1])
    if (clim_val == (0,0)):
        print "Default colour limits"
        im.set_clim(0, np.max(raster))
    else:
        print "Now setting colour limits to "+str(clim_val[0])+" and "+str(clim_val[1])
        im.set_clim(clim_val[0],clim_val[1])
    
    
    cbar = fig.colorbar(im, orientation='vertical')
    cbar.set_label(colorbarlabel)  
    
    #set the file format
    fformat = 'svg'      

    figname = "Spatial"+FilePrefix+"_gray."
    figname = figname+fformat
    print "The figure name is: "+figname
    plt.savefig(figname, format=fformat) 
    plt.close("all")

#==============================================================================

if __name__ == "__main__":

    # For the Manuscript I was working in Windows, so the folder seperations
    # Are `//`. If you work in Linux these van be changed to '\'. 
    DataDirectory = "C://basin_data//Model_results//June2015_Results//HighK//Select_slices//" 
    FilenamePrefix = "CRNVF_long_HighK_"
    metadata_prefix = "CRNVF_long_HighK_"
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 237
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (1,0,0)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 224
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (1,0,0)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)    
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 212
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (1,0,0)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)      
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 199
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (1,0,0)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)     
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 237
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (0,1,1)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 224
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (0,1,1)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)    
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 212
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (0,1,1)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)      
    
    # Time slices used in paper are 199, 212, 224 and 237 corresponding
    # to 400, 425, 450 and 475 kyr    
    time_slice = 199
    
    # Variation flag (1,0,0) is for uplift variation
    # (0,1,1) is both K and D variability. 
    # (0,1,0) would be for K only, and (0,0,1) woudl be for D only
    variation_flags = (0,1,1)
    Erosion_plots(DataDirectory,FilenamePrefix,metadata_prefix,time_slice,variation_flags)         
    