#rhs.py builds the right hand side of the voltage equation given that the gating variables have been updated
# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
import numpy as np
import scipy as sp
import parameters as par
import gating_coefficients as gc

Aj = gc.Aj
Ae = gc.Ae
grid = par.grid
CN = par.CN
CM = par.CM
dxa = par.dxa
dxp = par.dxp
dt = par.dt
ra = par.ra
rp = par.rp
rhoa = par.rhoA
rhop = par.rhoP
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
def maked(m,n,h):

# makeb updates the coefficients of the main diagonal since it's a function of the gating variables
def makeb(g):
    b = [0]*n
    for i in range(n):
        if grid[i] == 0:    #active cable
            b[i] = (CN/dt + g[i]/2. + ra/(2*rhoa*dxa**2))
        elif grid[i] == 1:    #passive cable
            b[i] = (CM/dt + g[i]/2. + rp/(2*rhop*dxp**2))
        elif grid[i] == 2:      # active to passive junction
            b[i] = (Aj*CM/dt + Aj*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa) + np.pi*rp**2/(2*rhop*dxp))
        elif grid[i] == 3:     # passive to active junction    
            b[i] = (Aj*CM/dt + Aj*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa) + np.pi*rp**2/(2*rhop*dxp))
        elif grid[i] == 4  or grid[i] == 5:   #start point or end point
            b[i] = (Ae*CN/dt + Ae*g[i]/2 + np.pi*ra**2/(2*rhoa*dxa))
    return b
