#Implements a Gaussian elimination solver
import numpy as np
import scipy as sp
import parameters as par

n = par.n             #import number of spatial discretizations


def tridiagonalSolve(a,b,c,d):
    print "b is" + str(b)
    T = np.zeros([n,n]) #create nxn tridiagonal matrix
    for i in range(n):      #fill in the T matrix using 'a','b','c'
        T[i,i] = b[i]
        if i != 0:
            T[i,i-1] = a[i]
        if i != n-1:
            T[i,i+1] = c[i]
    print "calling tridiagonal solve"
    return np.linalg.solve(T,d)

