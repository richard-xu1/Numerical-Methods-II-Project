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

#Movieimport matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

n = par.n
x_axis = np.linspace(1,n,num=n,endpoint=True)
print "x_axis is" +str(x_axis)
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

#TimeStep
print "v0 is " + str(v_k)
frame = 0
while t < T:
    N_kh = TimeStep(N_kh,1,v_k) #Timestep in n
    M_kh = TimeStep(M_kh,2,v_k) #Timestep in m
    H_kh = TimeStep(H_kh,3,v_k) #Timestep in h
    g,E = calc_gate_coeff(N_kh,M_kh,H_kh)		
    b= makeb(g)                  #Update b
    current= par.injectedCurrent(t+0.5*dt)      #compute current
    d= maked(v_k,g,E,current)           #Update d
    v_k = tridiagonalSolve(a,b,c,d)  #Solve Tridiagonal system
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
    titleString = 't=%8.2f ,dt=%8.4f' % (t,dt)
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
anim.save('test.mp4',writer=writer,dpi=dpi)

plt.show()