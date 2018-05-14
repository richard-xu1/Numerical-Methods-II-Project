# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import time
import numpy as np
import scipy as sp
import parameters as par
from gating_time_step import TimeStep,Initialize
from Coefficients import makeCoefficients
#from Tridiagonal_Solver import tridiagonalSolve
from linear_tridiagonal_solve import tridiagonalSolve
from rhs_diagonal import maked,makeb
from gating_coefficients import calc_gate_coeff
cimport numpy as np

#Movieimport matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

def main():
    startTime= time.time()
    caseNumber = par.caseNumber
    cdef int n = par.n
    cdef np.ndarray x_axis = np.linspace(1,n,num=n,endpoint=True)
    cdef np.ndarray grid = par.grid

    cdef float v_rest = par.v_rest
    cdef float dt = par.dt
    cdef float Tf = par.Tf
    cdef float T = par.T
    cdef int nf  = int(T/Tf)+1

    cdef np.ndarray v_k = np.ndarray(n)        #array stires voltage at time k
    #Initial conditions
    #Initialize all vectors to zero
    cdef Py_ssize_t i
    for i in range(0,n):
      v_k[i] = v_rest
      

    #Initialize Gating variable vectors. Gating variables need to be initialized to rest potentials. page 11, eq 29,30
    cdef np.ndarray N_kh = Initialize(v_k,1)
    cdef np.ndarray M_kh = Initialize(v_k,2)
    cdef np.ndarray H_kh = Initialize(v_k,3)

    #Initialize coefficient diagonals arrays
    cdef np.ndarray a
    cdef np.ndarray c
    a,c = makeCoefficients()

    cdef np.ndarray vFrames = np.ndarray([ nf, n])

    cdef int t_steps = par.tsteps
    cdef float t    = 0.    #   time since the beginning of the simulation
    cdef float tf   = 0.    #   time since the beginning of the frame
    cdef np.ndarray ta = np.zeros(t_steps/10+1)  # array for storing the time
    cdef np.ndarray vta = np.zeros(t_steps/10+1)	# array for storing time course of v
    cdef Py_ssize_t a_index = 0
    cdef Py_ssize_t j_index = 0
    cdef Py_ssize_t p_index = 0
    cdef np.ndarray vtp
    cdef np.ndarray vtj
    cdef np.ndarray conv_std = np.zeros(nf)
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
    #TimeStep
    frame = 0
    k = 0
    j = 0 
    cdef np.ndarray b
    cdef np.ndarray d
    while t < T:
        N_kh = TimeStep(N_kh,1,v_k,case) #Timestep in n

        M_kh = TimeStep(M_kh,2,v_k,case) #Timestep in m

        H_kh = TimeStep(H_kh,3,v_k,case) #Timestep in h

        g,E = calc_gate_coeff(N_kh,M_kh,H_kh)		

        b= makeb(g,case)                  #Update b
        current= par.injectedCurrent(t+0.5*dt)      #compute current
        d= maked(v_k,g,E,current,case)           #Update d
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
 



    # print "v is " + str(v_k)
    duration = time.time() - startTime
    midTime= time.time()
    print "Computations before Movie took" + str(duration)
    # Time Course Graphs of active, passive and junction nodes
    # print "va is " + str(vta)
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
