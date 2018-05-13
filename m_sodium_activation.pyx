import numpy as np
import scipy as sp
cimport numpy as np
# the equations for the sodium activation variable "m"

def alpha(v):
    cdef np.ndarray am = ((v + 45.)/10.)/(1 - np.exp(-(v+45.)/10.))
    return am
    
def beta(v):
    cdef np.ndarray bm = 4.*np.exp(-(v+70.)/18.)
    return bm
