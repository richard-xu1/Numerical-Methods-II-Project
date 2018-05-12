import numpy as np
import scipy as sp
# the equations for the potassium activation gating variable "n"

def alpha(v):
    an = (0.1)*((v+60.)/10.)/(1 - np.exp(-(v+60.)/10.))
    return an
    
def beta(v):
    bn = (0.125)*np.exp(-(v+70.)/80.)
    return bn
    
