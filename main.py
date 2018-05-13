# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import time
import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients
from Tridiagonal_Solver import tridiagonalSolve
from rhs_diagonal import maked,makeb
from gating_coefficients import Aj,Ae,calc_gate_coeff

n = par.n
v_rest = par.v_rest
dt = par.dt
#Initialize Arrays
# N_kh = np.ndarray(n)       #array stores gating variable n at time k+1/2
# M_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2
# H_kh = np.ndarray(n)       #array stores gating variable m at time k+1/2

v_k = np.ndarray(n)        #array stires voltage at time k

#Initial conditions
#Initialize all vectors to zero
for i in range(0,n):
  v_k[i] = v_rest
  
#Initialize Gating variable vectors. Gating variables need to be initialized to rest potentials. page 11, eq 29,30
N_kh = Initialize(v_k,1)
M_kh = Initialize(v_k,2)
H_kh = Initialize(v_k,3)

# print "n is" + str(N_kh)
# print "m is" + str(M_kh)
# print "H is" + str(H_kh)


#Initialize coefficient diagonals arrays

start = time.time()
a,c = makeCoefficients()
duration = time.time() - start
start=time.time()
print"A Code time" + str(duration)
#Compute coefficient diagonals

t_steps = par.tsteps

t = 0
#TimeStep
print "v0 is " + str(v_k)
for k in range (100000):
	start=time.time()
	#Update gating variables
	# print "Time is" + str(t)
	N_kh = TimeStep(N_kh,1,v_k) #Timestep in n
	duration = time.time() - start
	start=time.time()
	print"N Code time" + str(duration)
	M_kh = TimeStep(M_kh,2,v_k) #Timestep in m
	duration = time.time() - start
	start=time.time()
	print"M Code time" + str(duration)
	H_kh = TimeStep(H_kh,3,v_k) #Timestep in h
	duration = time.time() - start
	start=time.time()
	print"H Code time" + str(duration)
	# print "n is" + str(N_kh)
	# print "m is" + str(M_kh)
	# print "H is" + str(H_kh)
	g,E = calc_gate_coeff(N_kh,M_kh,H_kh)
	duration = time.time() - start
	start=time.time()
	print"G Code time" + str(duration)

	
	b= makeb(g)  #Update b
	duration = time.time() - start
	start=time.time()
	print"B Code time" + str(duration)

	current= par.injectedCurrent(t+0.5*dt)

	d= maked(v_k,g,E,current)#Update d
	duration = time.time() - start
	start=time.time()
	print"D Code time" + str(duration)
	#   d = np.random.random(d.shape)
	v_k = tridiagonalSolve(a,b,c,d)  #Solve Tridiagonal system
	t = t + dt
	if k%1000==0 :
	  print "T is" +str(t)
	  print "v is" +str(v_k)
print "vk is " + str(v_k)

