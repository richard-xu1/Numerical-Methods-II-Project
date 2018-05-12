import numpy as np
import scipy as sp
# the equations for the sodium inactivation gating variable "h"

def alpha(v):
    ah = 0.07*np.exp(-(v+70.)/20. )
    return ah
    
def beta(v):
    bh = 1/(1 + np.exp(-(v+40.)/10.))
    return bh
    
    
