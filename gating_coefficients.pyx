# makes the gating coefficients g,E,g_tilde, E_tilde and also defines the data field Ao which can be imported to make the tridiagonal system

import parameters as par
import numpy as np
import scipy as sp
cimport numpy as np

cdef np.ndarray grid = par.grid
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

Aj = np.pi*(ra*dxa + rp*dxp)    #A_tilde on a junction
Ae = np.pi*ra*dxa               #A_tilde on a boundary point

#define the returned variables
cdef np.ndarray g = np.zeros(n)
cdef np.ndarray E = np.zeros(n)

def calc_gate_coeff(N,m,h):
    cdef Py_ssize_t i
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
        if grid[i] == 2:
            g[i] = (np.pi*(rp*dxp*g[i+1] + ra*dxa*g[i-1]))/Aj
            E[i] = (np.pi*(rp*dxp*g[i+1]*E[i+1] + ra*dxa*g[i-1]*E[i-1]))/(Aj*g[i])
        elif grid[i] == 3:
            g[i] = (np.pi*(rp*dxp*g[i-1] + ra*dxa*g[i+1]))/Aj
            E[i] = (np.pi*(rp*dxp*g[i-1]*E[i-1] + ra*dxa*g[i+1]*E[i+1]))/(Aj*g[i])       
        elif grid[i] == 4:
            g[i] = g[i+1]
            E[i] = E[i+1]
        elif grid[i] == 5:
            g[i] = g[i-1]
            E[i] = E[i-1]
    return g,E
         
            
