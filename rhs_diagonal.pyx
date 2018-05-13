#rhs.py builds the right hand side of the voltage equation given that the gating variables have been updated
# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import numpy as np
import scipy as sp
import parameters as par
from parameters import injectedCurrent as current
import gating_coefficients as gc
cimport numpy as np

cdef float Aj = gc.Aj
cdef float Ae = gc.Ae
cdef np.ndarray grid = par.grid
cdef float CN = par.CN
cdef float CM = par.CM
cdef float dxa = par.dxa
cdef float dxp = par.dxp
cdef float dt = par.dt
cdef float ra = par.ra
cdef float rp = par.rp
cdef float rhoa = par.rhoA
cdef float rhop = par.rhoP
cdef int n = par.n

#rhs of interior nodes depends on, v_j^k, v_j+1^k, v_j-1^k, g_j^k+(^(k1/2), E_j^k+(1/2)
#g_j^k+(1/2) Can be computed from the gating variables , p8, eq 20
#E_j^k+(1/2) can be computed from the gating variables , p8 ,eq 21

#rhs of junction points depends on Atilde_j, gtilde_j^k+(1/2),Etilde_j^k+(1/2) v_j^k, v_j+1^k, v_j-1^k, 
#Atilde_j can be computed from constants
#gtilde_j needs can be computed from gating variables, Type 2/3 equations
#Etilde_j needs can be computed from gating variables, Type 2/3 equations

#rhs of boundary points depends on 
#j=0: Atilde_0, gtilde_0^k+(1/2),Etilde_0^k+(1/2) v_0^k, v_1^k, i_0(t) (injected current) 
#j=n-1: Atilde_n-1, gtilde_n-1^k+(1/2),Etilde_n-1^k+(1/2) v_n-1^k, v_n-2^k

#maked would need the updated gating variables, and other parameters to compute the RHS coefficient
def maked(v,g,E,current):
    cdef np.ndarray[double,ndim=1] d = np.zeros(n)
    cdef Py_ssize_t i
    
    for i in range(n):
        if grid[i] == 0:    #Active internal
            vjkterm = (CN/dt)-(ra/(2*rhoa*dxa*dxa))
            vjothers= ra/(4*rhoa*dxa*dxa)
            d[i] = (vjkterm-g[i]/2)*v[i]+vjothers*v[i+1]+vjothers*v[i-1]+g[i]*E[i]

        elif grid[i] == 1:  #Passive internal
            vjkterm = (CM/dt)-(rp/(2*rhop*dxp*dxp))
            vjothers= rp/(4*rhop*dxp*dxp)
            d[i] = (vjkterm-g[i]/2)*v[i]+vjothers*v[i+1]+vjothers*v[i-1]+g[i]*E[i]

        elif grid[i] == 2:   #Active to Passive
            vjkterm=(Aj*CM/dt)-np.pi*rp*rp/(2*rhop*dxp)-(np.pi*ra*ra/(2*rhoa*dxa))
            vp = (np.pi*rp*rp)/(2*dxp*rhop)
            va = (np.pi*ra*ra)/(2*dxa*rhoa)
            d[i] = (vjkterm-(Aj*g[i]/2))*v[i] + va*v[i-1] + vp*v[i+1] +Aj*g[i]*E[i]

        elif grid[i] == 3:  #Passive to Active
            vjkterm=(Aj*CM/dt)-np.pi*rp*rp/(2*rhop*dxp)-(np.pi*ra*ra/(2*rhoa*dxa))
            vp = (np.pi*rp*rp)/(2*dxp*rhop)
            va = (np.pi*ra*ra)/(2*dxa*rhoa)
            d[i] = (vjkterm-(Aj*g[i]/2))*v[i] + va*v[i+1] + vp*v[i-1] +Aj*g[i]*E[i]

        elif grid[i] == 4:  
            vjkterm=(Ae*CN/dt)-(np.pi*ra*ra/(2*rhoa*dxa))
            va = (np.pi*ra*ra)/(2*dxa*rhoa)
            d[i] = (vjkterm-(Ae*g[i]/2))*v[i] + va*v[i+1] + Ae*g[i]*E[i] +current
        else:
            vjkterm=(Ae*CN/dt)-(np.pi*ra*ra/(2*rhoa*dxa))
            va = (np.pi*ra*ra)/(2*dxa*rhoa)
            d[i] = (vjkterm-(Ae*g[i]/2))*v[i] + va*v[i-1] + Ae*g[i]*E[i] 
    return d

# makeb updates the coefficients of the main diagonal since it's a function of the gating variables
def makeb(g):
    cdef np.ndarray[double,ndim=1] b = np.zeros(n)
    cdef Py_ssize_t i
    for i in range(n):
        if grid[i] == 0:    #active cable
            b[i] = (CN/dt + g[i]/2. + ra/(2*rhoa*dxa**2))
        elif grid[i] == 1:    #passive cable
            b[i] = (CM/dt + g[i]/2. + rp/(2*rhop*dxp**2))
        elif grid[i] == 2:      # active to passive junction
            b[i] = (Aj*CM/dt + Aj*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa) + np.pi*rp**2/(2*rhop*dxp))
        elif grid[i] == 3:     # passive to active junction    
            b[i] = (Aj*CM/dt + Aj*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa) + np.pi*rp**2/(2*rhop*dxp))
        else:  #start point or end point
            b[i] = (Ae*CN/dt + Ae*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa))
    # print "g was" + str(g)
    return b
