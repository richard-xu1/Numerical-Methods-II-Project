import numpy as np
import scipy as sp
# the equations for the sodium inactivation gating variable "h"

# coefficients used in alpha/beta functions
Aa = 0.1     #1/msec
Ba = -10.    #mV
Ca = 6.      #mvV
Ab = 4.5     #1/msec
Bb = 45.      #mV
Cb = 10.      #mV   

def alpha(v):
    ah = Aa*(Ba-v)/(1 - np.exp((v-Ba)/Ca))
    return ah
    
def beta(v):
    bh = Ab/( 1 + np.exp((Bb-v)/Cb))
    return bh
    
    
