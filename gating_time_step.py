import numpy as np
import scipy as sp
import h_sodium_inactivation as h
import m_sodium_activation as m
import n_potassium_activation as n
import parameters as par

# timestep for the gating variables
dt = par.dt
dx = par.dx
n = par.n
invdt = np.full((nx,1),1/dt) #create a nx by 1 list full of 1/dt for element wise addition/subtraction in calculation c1 and c2

def TimeStep(s,type,v): #n is type = 1, m is type = 2, h is type = 3
    #takes s_k and v_{k+1/2} and returns s_{k+1}  
    #define alpha and beta functions for the gate type
    def alpha(v):
        if type == 1:  
            return n.alpha(v)
        elif type == 2:
            return m.alpha(v)
        else:
            return h.alpha(v)
    def beta(v):
        if type == 1:  
            return n.beta(v)
        elif type == 2:
            return m.beta(v)
        else:
            return h.beta(v)     

    A = alpha(v)                 #calculate and store alpha(v)
    B = beta(v)                  #calculate and store beta(v)
    C1 = invdt + A/2 + B/2
    C2 = invdt - A/2 - B/2
    return np.divide((np.multiply(s,C2) + A),C1)
        
  
