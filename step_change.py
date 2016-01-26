# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:47:25 2016

@author: smudd
"""

import numpy as np

def step_change(lambda1, lambda2,eold,A,dbr,t_vec):
    
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
    eold = 0.0026
    A = 2
    
    dbr = 150.0
    t = np.asarray(t_vec)
    step_change(lambda1, lambda2,eold,A,dbr,t)         
       
    