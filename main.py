import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients

n = par.n
#Initialize Arrays

M_k = np.ndarray(n)       #array stores gating variable m at time k
M_kHalf = np.ndarray(n)   #array stores gating variable m at time k+1/2


N_k = np.ndarray(n)       #array stores gating variable n at time k
N_kHalf = np.ndarray(n)   #array stores gating variable n at time k+1/2

H_k = np.ndarray(n)       #array stores gating variable m at time k
H_kHalf = np.ndarray(n)   #array stores gating variable m at time k+1/2


v_k = np.ndarray(n)
v_kHalf = np.ndarray(n)

#Initial conditions
#Initialize all vectors to zero
for i in range(0,n):
    v_k[i] = 0.
    v_kHalf[i] = 0.
    N_k[i] = 0.
    N_kHalf[i] = 0.
    M_k[i] = 0.
    M_kHalf[i] = 0.
    H_k[i] = 0.
    H_kHalf[i] = 0.
#Initialize Gating variable vectors
Initialize(N_k,1)
Initialize(N_kHalf,1)
Initialize(M_k,2)
Initialize(M_kHalf,2)
Initialize(H_k,3)
Initialize(H_kHalf,3)

#Initialize coefficient diagonals
a=np.ndarray(n)
b=np.ndarray(n)
C=np.ndarray(n)

#Compute coefficient diagonals
a,b,c = makeCoefficients(a,b,c)

#TimeStep
for k in range (t_steps)
  #Update gating variables  
  N_k = TimeStep(N_k,1,v_kHalf)
  M_k = TimeStep(M_k,2,v_kHalf)
  H_k = TimeStep(H_k,3,v_kHalf)

  d= makeD(v_k, v_khalf,M_khalf,N_khalf,H_khalf)
  
  v_k = tridiagonalSolve(a,b,c,d)
 
  N_kHalf = TimeStep(N_kHalf,1,v_k)
  M_kHalf = TimeStep(M_kHalf,2,v_k)
  H_kHalf = TimeStep(H_kHalf,3,v_k)
  
  dHalf=makeD(v_khalf,v_k,M_k,N_k,H_k)
  v_kHalf = tridiagonalSolve(a,b,c,dHalf)
  
