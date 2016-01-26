# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:47:25 2016

@author: smudd
"""

import numpy as np

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
        

    print ratios
    return ratios
    
    #top_time_vec2 = np.exp( np.divide(Gamma,np.add( dbr/Gamma,np.multiply(t_vec,(eros+Gamma*lambda1)))))
    #bottom_time_vec2 = np.exp( np.divide(Gamma,np.add( dbr/Gamma,np.multiply(t_vec,(eros+Gamma*lambda2)))))
    
    #print top_time_vec2
    #print bottom_time_vec2 

if __name__ == "__main__":
    lambda1 = 121.0*(10**-6)
    lambda2 = 456*(10**-9)
    Gamma = 160.0
    t_vec = [500, 5000]
    eros = 0.0026
    dbr = 150.0
    t = np.asarray(t_vec)
    block_removal(lambda1, lambda2,eros,dbr,t)         
       
    