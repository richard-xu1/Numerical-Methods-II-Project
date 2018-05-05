import numpy as np
import scipy as sp
import parameters 

s_k = np.ndarray(n)
s_kHalf = np.ndarray(n)

v_k = np.ndarray(n)
v_kHalf = np.ndarray(n)

gatingVarSolve(s_k,s_kHalf)
tridiagonalsolve(a,b,c,d)
