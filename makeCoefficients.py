import numpy as np
import scipy as sp
import parameters par


r = par.r
rho = par.rho
cn = par.CN
cm = par.CM
dx= par.dx
dt= par.dt
r1 = par.r1
r2 = par.r2

grid=par.grid

#Interior Points
for i in range(1,n-1)
  if grid[i] == false
    a[i]= -r/(4*rho*dx*dx)
    b[i]= cn/dt + r/(2*rho*dx*dx) 
    c[i]= -r/(4*rho*dx*dx)
  else 
    a[i]= -1./(2*dx*dx(r1+r2))
    b[i]= cm/dt + 1./(dx*dx*(r1+r2))
    c[i]= -1./(2*dx*dx(r1+r2))
    
#Boundary Points
b[0] = 
c[0] = 

a[n-1] = 
b[n-1] =

  


