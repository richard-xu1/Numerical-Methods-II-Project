# this code should only construct a and c vectors since they are constants
# b is a function of gating variables so it needs to be updated with each time step

import numpy as np
import scipy as sp
import parameters as par

def makeCoefficients(a,c):
	r = par.r
	rho = par.rho
	cn = par.CN
	cm = par.CM
	dx= par.dx
	dt= par.dt
	r1 = par.r1
	r2 = par.r2
	n = par.n

	grid=par.grid

	#Interior Points
	for i in range(1,n-1):
	  if grid[i] == False:
	    a[i]= -r/(4*rho*dx*dx)
	    c[i]= -r/(4*rho*dx*dx)
	  else:
	    a[i]= -1./(2*dx*dx*(r1+r2))
	    c[i]= -1./(2*dx*dx*(r1+r2))
	    
	#Boundary Points

	c[0] = 0
	a[n-1] = 0 

  


