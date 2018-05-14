#Implements a Gaussian elimination solver
import numpy as np
import scipy as sp
import parameters as par
cimport numpy as np


def tridiagonalSolve(a,b,c,d):
    cdef int n = par.n             #import number of spatial discretizations
    cdef np.ndarray T = np.zeros([n,n]) #create nxn tridiagonal matrix
    cdef Py_ssize_t i
    for i in range(n):      #fill in the T matrix using 'a','b','c'
        T[i,i] = b[i]
        if i != 0:
            T[i,i-1] = a[i]
        if i != n-1:
            T[i,i+1] = c[i]
    # print "T is"+str(T)
    # print "d is"+str(d)
    return np.linalg.solve(T,d)

