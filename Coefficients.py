# makeCoefficients makes computes coefficients vectors a and c for different types of nodes


import numpy as np
import scipy as sp
import parameters as par

def makeCoefficients(a,c):
	ra = par.ra
    rp = par.rp
	rhoa = par.rhoA
	rohp = par.rhoA
	cn = par.CN
	cm = par.CM
	dxa = par.dxa
	dxp = par.dxp
	n = par.n
	grid=par.grid

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
            a[i]= -(np.pi*ra)/(2*rhoa*dxa)
            c[i]= -(np.pi*rp)/(2*rhop*dxp)
        elif grid[i] ==3:   #passive to active
            a[i]= -(np.pi*rp)/(2*rhop*dxp)
            c[i]= -(np.pi*ra)/(2*rhoa*dxa)
	    
	#Boundary Points

	c[0] = -(np.pi*ra)/(2*rhoa*dxa)
	a[n-1] = -(np.pi*ra)/(2*rhoa*dxa)
	
	

  


