# makeCoefficients makes computes coefficients vectors a and c for different types of nodes

import numpy as np 
import scipy as sp
import parameters as par
cimport numpy as np

# DTYPE = np.float
# ctypedef np.float
def makeCoefficients():
    cdef float ra = par.ra
    cdef float rp = par.rp
    cdef float rhoa = par.rhoA
    cdef float rhop = par.rhoP
    cdef float cn = par.CN
    cdef float cm = par.CM
    cdef float dxa = par.dxa
    cdef float dxp = par.dxp
    cdef int n = par.n
    cdef np.ndarray[np.float64_t,ndim=1] grid=par.grid  
    cdef np.ndarray[np.float64_t,ndim=1] a=np.ndarray(n)
    cdef np.ndarray[np.float64_t,ndim=1] c=np.ndarray(n)
    # assert a.dtype == DTYPE and c.dtype == DTYPE
    cdef Py_ssize_t i
    #Interior Points
    for i in range(1,n-1):
    # 0: active cable internal, 1: passive internal, 2: active to passive
    # 3: passive to active, 4: start point, 5: end point	
        if grid[i] == 0:    #active internal
            a[i]= -ra/(4*rhoa*dxa*dxa)
            c[i]= -ra/(4*rhoa*dxa*dxa)
        elif grid[i] ==1:   #passive internal
            a[i]= -rp/(4*rhop*dxp*dxp)
            c[i]= -rp/(4*rhop*dxp*dxp)
        elif grid[i] ==2:   #active to passive
            a[i]= -(np.pi*ra*ra)/(2*rhoa*dxa)
            c[i]= -(np.pi*rp*rp)/(2*rhop*dxp)
        elif grid[i] ==3:   #passive to active
            a[i]= -(np.pi*rp*rp)/(2*rhop*dxp)
            c[i]= -(np.pi*ra*ra)/(2*rhoa*dxa)
        
    #Boundary Points

    c[0] = -(np.pi*ra*ra)/(2*rhoa*dxa)
    a[n-1] = -(np.pi*ra*ra)/(2*rhoa*dxa)
    
    return a,c
