import numpy as np
import scipy as sp
# the equations for the sodium inactivation gating variable "h"

# coefficients used in alpha/beta functions
A = 0.1     #1/msec
B = -10.    #mV
C = 6.      #mvV

def alpha(v):
    ah = A*(B-V)/(1 - np.exp((v-B)/C)
    return ah
    
def beta(v):
    bh = A/( 1 + np.exp((B-v)/C))
    return bh
    
    
