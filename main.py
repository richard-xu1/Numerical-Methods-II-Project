# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import time
import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients
# from Tridiagonal_Solver import tridiagonalSolve
from linear_tridiagonal_solve import tridiagonalSolve
from rhs_diagonal import maked,makeb
from gating_coefficients import Aj,Ae,calc_gate_coeff

#Movieimport matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

caseNumber = par.caseNumber
n = par.n
x_axis = np.linspace(1,n,num=n,endpoint=True)
grid = par.grid

v_rest = par.v_rest
dt = par.dt
Tf = par.Tf
T = par.T
nf  = int(T/Tf)+1

v_k = np.ndarray(n)        #array stires voltage at time k
#Initial conditions
#Initialize all vectors to zero
for i in range(0,n):
  v_k[i] = v_rest
  

#Initialize Gating variable vectors. Gating variables need to be initialized to rest potentials. page 11, eq 29,30
N_kh = Initialize(v_k,1)
M_kh = Initialize(v_k,2)
H_kh = Initialize(v_k,3)



#Initialize coefficient diagonals arrays

a,c = makeCoefficients()

vFrames = np.ndarray([ nf, n])

t_steps = par.tsteps
t    = 0.    #   time since the beginning of the simulation
tf   = 0.    #   time since the beginning of the frame
ta = np.zeros(t_steps/10+1)  # array for storing the time
vta = np.zeros(t_steps/10+1)	# array for storing time course of v
a_index = 0
j_index = 0
p_index = 0
for i in range(n/3,n):
	if grid[i] == 0:
		a_index = i;
		break;
if caseNumber == 1:
	vtp = np.zeros(t_steps/10+1)
	vtj = np.zeros(t_steps/10+1)
	for i in range(n/3,n):
		if grid[i] == 2:
			j_index = i
		if grid[i] == 1:
			p_index = i	
		if p_index != 0 and j_index != 0:
			break;
print "a_index is " + str(a_index)
print "p_index is " + str(p_index)
print "j_index is " + str(j_index)
#TimeStep
print "v0 is " + str(v_k)
frame = 0
k = 0
j = 0 
while t < T:
    N_kh = TimeStep(N_kh,1,v_k) #Timestep in n
    M_kh = TimeStep(M_kh,2,v_k) #Timestep in m
    H_kh = TimeStep(H_kh,3,v_k) #Timestep in h
    g,E = calc_gate_coeff(N_kh,M_kh,H_kh)		
    b= makeb(g)                  #Update b
    current= par.injectedCurrent(t+0.5*dt)      #compute current
    d= maked(v_k,g,E,current)           #Update d
    v_k = tridiagonalSolve(a,b,c,d)  #Solve Tridiagonal system
    if k % 10 == 0:
	    ta[j] = t  
	    vta[j] = v_k[a_index]
	    if caseNumber == 1:
	    	vtp[j] = v_k[p_index]
	    	vtj[j] = v_k[j_index]
	    j = j+1
    k = k + 1
    t = t + dt    
    tf= tf+ dt 
    print "t is" + str(t)
    # print "v_k is"+str(v_k)
    if tf > Tf:
        print "saving frame no" +str(frame)
        vFrames[frame, :] = v_k
        frame = frame+1
        tf=0.


print "v is " + str(v_k)

# Time Course Graphs of active, passive and junction nodes
print "va is " + str(vta)
plt.figure()
plt.plot(ta,vta,Lw = 1)
plt.title('v_active (mV) vs time (ms)')
plt.show()

if caseNumber == 1:
	print "vp is " + str(vtp)
	plt.figure()
	plt.plot(ta,vtp,Lw = 1)
	plt.title('v_passive (mV) vs time (ms)')
	plt.show()
	print "vj is " + str(vtj)
	plt.figure()
	plt.plot(ta,vtj,Lw = 1)
	plt.title('v_junction (mV) vs time (ms)')
	plt.show()
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=2)  

def init():
    line.set_data([], [])
    return line,

def animate(i): 
    z = vFrames[i,:]
    # print  "z is" + str(z)
    t = Tf*i
    titleString = 't=%8.2f ,dt=%8.4f,cablelength=%8.2f' % (t,dt,par.cableLength)
    line.set_data(x_axis,z)
    plt.title(titleString)
    plt.xlim(0., n)
    plt.ylim(-100,100)
    # plt.show()
    return line,  


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nf)

dpi = 200
writer = animation.writers['ffmpeg'](fps=10)
anim.save('MyelinatedHH.mp4',writer=writer,dpi=dpi)

plt.show()