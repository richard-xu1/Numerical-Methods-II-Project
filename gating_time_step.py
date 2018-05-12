#Update gating variable's
#Internal points in active and passive cable get updated according to equation for s^(k+1/2)

# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point

import numpy as np
import scipy as sp
import h_sodium_inactivation as h
import m_sodium_activation as m
import n_potassium_activation as n
import parameters as par

# timestep for the gating variables
dt = par.dt
dx = par.dx
N = par.n
invdt = np.full((N,1),1/dt) #create a nx by 1 list full of 1/dt for element wise addition/subtraction in calculation c1 and c2

def Initialize(v,gtype):
    def alpha(v):
            if gtype == 1:  
                return n.alpha(v)
            elif gtype == 2:
                return m.alpha(v)
            else:
                return h.alpha(v)
    def beta(v):
        if gtype == 1:  
            return n.beta(v)
        elif gtype == 2:
            return m.beta(v)
        else:
            return h.beta(v)
    v = (np.divide(alpha(v),(alpha(v)+beta(v))))

def TimeStep(s,gtype,v): #n is type = 1, m is type = 2, h is type = 3
    #takes s_k and v_{k+1/2} and returns s_{k+1}  
    #define alpha and beta functions for the gate type
    if gtype == 1:  
        A = n.alpha(v)                 #calculate and store alpha(v)
        B = n.beta(v)                  #calculate and store beta(v)
    elif gtype == 2:
        A = m.alpha(v)                 #calculate and store alpha(v)
        B = m.beta(v)                  #calculate and store beta(v)
    else:
        A = h.alpha(v)                 #calculate and store alpha(v)
        B = h.beta(v)                  #calculate and store beta(v)
    C1 = invdt + A/2 + B/2
    C2 = invdt - A/2 - B/2
    return np.divide((np.multiply(s,C2) + A),C1)
        
   
