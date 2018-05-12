# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients
from Tridiagonal_Solver import tridiagonalSolve
from rhs import maked,makeb
from gatingCoefficients import Aj,Ae

n = par.n
v_rest = par.v_rest
#Initialize Arrays
N_kh = np.ndarray(n)       #array stores gating variable n at time k+1/2
M_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2
H_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2


v_k = np.ndarray(n)        #array stires voltage at time k

#Initial conditions
#Initialize all vectors to zero
for i in range(0,n):
    v_k[i] = v_rest.
    N_kh[i] = 0.
    M_kh[i] = 0.
    H_kh[i] = 0.
    
#Initialize Gating variable vectors. Gating variables need to be initialized to rest potentials. page 11, eq 29,30
Initialize(N_kh,1)
Initialize(M_kh,2)
Initialize(H_kh,3)

#Initialize coefficient diagonals arrays
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
  N_kh = TimeStep(N_kh,1,v_kHalf) #Timestep in n
  M_kh = TimeStep(M_kh,2,v_kHalf) #Timestep in m
  H_kh = TimeStep(H_kh,3,v_kHalf) #Timestep in h
  g,E = richardsfunc(N_kh,M_kh,H_kh)
  b= makeb(g)  #Update b
  d= maked(v,g,E)#Update d
#   d = np.random.random(d.shape)
  v_k = tridiagonalSolve(a,b,c,d)  #Solve Tridiagonal system
  
print v_k
