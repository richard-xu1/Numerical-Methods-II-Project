import numpy as np
import scipy as sp
# the equations for the sodium activation variable "m"

def alpha(v):
    am = ((v + 45.)/10.)/(1 - np.exp(-(v+45.)/10.))
    return am
    
def beta(v):
    bm = 4.*np.exp(-(v+70.)/18.)
    return bm
