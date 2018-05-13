import numpy as np
import scipy as sp
cimport numpy as np
# the equations for the potassium activation gating variable "n"

def alpha(v):
    cdef np.ndarray an = (0.1)*((v+60.)/10.)/(1 - np.exp(-(v+60.)/10.))
    return an
    
def beta(v):
    cdef np.ndarray bn = (0.125)*np.exp(-(v+70.)/80.)
    return bn
    
