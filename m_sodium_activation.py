import numpy as np
import scipy as sp
# the equations for the sodium inactivation gating variable "h"

# coefficients used in alpha/beta functions
Aa = .36     #1/msec
Ba = 22.    #mV
Ca = 3.      #mvV
Ab = .4     #1/msec
Bb = 13.      #mV
Cb = 20.     #mV   

def alpha(v):
    am = Aa*(v-Ba)/(1 - np.exp((Ba-v)/Ca))
    return am
    
def beta(v):
    bm = Ab*(Bb - v)/( 1 - np.exp((v-Bb)/Cb))
    return bm
