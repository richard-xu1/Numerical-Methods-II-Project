import numpy as np
import scipy as sp
# the equations for the sodium inactivation gating variable "h"

# coefficients used in alpha/beta functions
Aa = .02     #1/msec
Ba = 35.    #mV
Ca = 10.      #mvV
Ab = .05     #1/msec
Bb = 10.      #mV
Cb = 10.     #mV   

def alpha(v):
    an = Aa*(v-Ba)/(1 - np.exp((Ba-v)/Ca))
    return an
    
def beta(v):
    bn = Ab*(Bb - v)/( 1 - np.exp((v-Bb)/Cb))
    return bn
    
