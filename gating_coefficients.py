# makes the gating coefficients g,E,g_tilde, E_tilde and also defines the data field Ao which can be imported to make the tridiagonal system

import parameters as par
import numpy as np
import scipy as sp

grid = par.grid
n = par.n
gNA_bar = par.gNA
gK_bar = par.gK
gL = par.gL
gNAp_bar = par.gNAp
gKp_bar = par.gKp
gLp = par.gLp
dxa = par.dxa
dxp = par.dxp
ra = par.ra
rp = par.rp
ENA = par.ENA
EK = par.EK
EL = par.EL

Aj = np.pi*(ra*dxa + rp*dxp)    #A_tilde on a junction
Ae = np.pi*ra*dxa               #A_tilde on a boundary point

#define the returned variables
g = [0]*n
E = [0]*n

def calc_gate_coeff(n,m,h):
    for i in range(n):
        if grid[i] == 0:
            gNA = gNA_bar*m[i]**3*h[i]
            gK  = gK_bar*n[i]**4
            g[i] = gNA + gK + gL
            E[i] = (gNA*ENA + gK*EK + gL*EL)/g[i]
        elif grid[i] == 1:
            gNA = gNAp_bar*m[i]**3*h[i]
            gK  = gKp_bar*n[i]**4
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
        else:
            g[i] = g[i-1]
            E[i] = E[i-1]
    return g,E
         
            
