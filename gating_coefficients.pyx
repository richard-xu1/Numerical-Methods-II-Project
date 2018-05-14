# makes the gating coefficients g,E,g_tilde, E_tilde and also defines the data field Ao which can be imported to make the tridiagonal system

import parameters as par
import numpy as np
import scipy as sp
cimport numpy as np


cdef int n = par.n
cdef float gNA_bar = par.gNA
cdef float gK_bar = par.gK
cdef float gL = par.gL
cdef float gNAp_bar = par.gNAp
cdef float gKp_bar = par.gKp
cdef float gLp = par.gLp
cdef float dxa = par.dxa
cdef float dxp = par.dxp
cdef float ra = par.ra
cdef float rp = par.rp
cdef float ENA = par.ENA
cdef float EK = par.EK
cdef float EL = par.EL
cdef float Aj = par.Aj
cdef float Ae = par.Ae

cdef float gNA
cdef float gK


DTYPE = np.float
#define the returned variables

def calc_gate_coeff(np.ndarray[np.float64_t, ndim=1] N,np.ndarray[np.float64_t, ndim=1] m,np.ndarray[np.float64_t, ndim=1] h):
    cdef np.ndarray[np.float64_t, ndim=1] g = np.zeros(n,dtype=DTYPE)
    cdef np.ndarray[np.float64_t, ndim=1] E = np.zeros(n,dtype=DTYPE)
    cdef np.ndarray[np.float64_t, ndim=1] grid = par.grid
    cdef Py_ssize_t i,j,k
    for i in range(n):
        if grid[i] == 0:
            gNA = gNA_bar*m[i]**3*h[i]
            gK  = gK_bar*N[i]**4
            g[i] = gNA + gK + gL
            E[i] = (gNA*ENA + gK*EK + gL*EL)/g[i]
        elif grid[i] == 1:
            gNA = gNAp_bar*m[i]**3*h[i]
            gK  = gKp_bar*N[i]**4
            g[i] = gNA + gK + gLp
            E[i] = (gNA*ENA + gK*EK + gLp*EL)/g[i]   
    for i in range(n):
        j=i-1
        k=i+1
        if grid[i] == 2:
            
            g[i] = (np.pi*(rp*dxp*g[k] + ra*dxa*g[j]))/Aj
            E[i] = (np.pi*(rp*dxp*g[k]*E[k] + ra*dxa*g[j]*E[j]))/(Aj*g[i])
        elif grid[i] == 3:
            j=i-1
            g[i] = (np.pi*(rp*dxp*g[j] + ra*dxa*g[k]))/Aj
            E[i] = (np.pi*(rp*dxp*g[j]*E[j] + ra*dxa*g[k]*E[k]))/(Aj*g[i])       
        elif grid[i] == 4:
            g[i] = g[k]
            E[i] = E[k]
        elif grid[i] == 5:
            g[i] = g[j]
            E[i] = E[j]
    return g,E
         
            
