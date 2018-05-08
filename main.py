import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients,makeb
from Tridiagonal_Solver import tridiagonalSolve
from rhs import maked

n = par.n
#Initialize Arrays
N_kh = np.ndarray(n)       #array stores gating variable n at time k+1/2
M_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2
H_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2


v_k = np.ndarray(n)        #array stires voltage at time k

#Initial conditions
#Initialize all vectors to zero
for i in range(0,n):
    v_k[i] = 0.
    N_kh[i] = 0.
    M_kh[i] = 0.
    H_kh[i] = 0.
    
\#Initialize Gating variable vectors. Gating variables need to be initialized to rest potentials. page 11, eq 29,30
Initialize(N_kh,1)
Initialize(M_kh,2)
Initialize(H_kh,3)

#Initialize coefficient diagonals
a=np.ndarray(n)
b=np.ndarray(n)
c=np.ndarray(n)
d=np.ndarray(n)

#Compute coefficient diagonals
makeCoefficients(a,c)
t_steps = int (par.T / par.dt) #make this more precise

#TimeStep
for k in range (t_steps):
  #Update gating variables  
  N_k = TimeStep(N_k,1,v_kHalf) #Timestep in n
  M_k = TimeStep(M_k,2,v_kHalf) #Timestep in m
  H_k = TimeStep(H_k,3,v_kHalf) #Timestep in h
  b= makeb(b,N_k,M_k,,H_k)  #Update b
  d= maked(d,v_k,N_k,M_k,H_k)   #Update d
  d = np.random.random(d.shape)
  v_k = tridiagonalSolve(a,b,c,d)  #Solve Tridiagonal system
  
print v_k
