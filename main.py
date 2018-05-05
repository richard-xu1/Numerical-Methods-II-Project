import numpy as np
import scipy as sp
import parameters 

#Initialize Arrays

M_k = np.ndarray(n)       #array stores gating variable m at time k
M_kHalf = np.ndarray(n)   #array stores gating variable m at time k+1/2


N_k = np.ndarray(n)       #array stores gating variable n at time k
N_kHalf = np.ndarray(n)   #array stores gating variable n at time k+1/2

H_k = np.ndarray(n)       #array stores gating variable m at time k
H_kHalf = np.ndarray(n)   #array stores gating variable m at time k+1/2


v_k = np.ndarray(n)
v_kHalf = np.ndarray(n)

a=np.ndarray(n)
b=np.ndarray(n)
C=np.ndarray(n)

a,b,c = makeCoefficients()

t_steps= T/dt
k_steps= 2*t_steps
for k in range (t_steps)
  #Update gating variables  
  N_k = gatingVarSolveH(N_k,1,v_kHalf)
  M_k = gatingVarSolveM(M_k,2,v_kHalf)
  H_k = gatingVarSolveN(H_k,3,v_kHalf)

  d= makeD(v_k, v_khalf,M_khalf,N_khalf,H_khalf)
  
  v_k = tridiagonalSolve(a,b,c,d)
 
  N_kHalf = gatingVarSolveH(N_kHalf,1,v_k)
  M_kHalf = gatingVarSolveM(M_kHalf,2,v_k)
  H_kHalf = gatingVarSolveN(H_kHalf,3,v_k)
  
  dHalf=makeD(v_khalf,v_k,M_k,N_k,H_k)
  v_kHalf = tridiagonalSolve(a,b,c,dHalf)
  
