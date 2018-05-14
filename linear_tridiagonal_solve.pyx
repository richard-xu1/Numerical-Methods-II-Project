#Implements a linear time tridiagonal Gaussian elimination solver
import numpy as np
import scipy as sp
import parameters as par
cimport numpy as np

cdef int n = par.n             #import number of spatial discretizations
DTYPE = np.float
def tridiagonalSolve(np.ndarray[np.float64_t, ndim=1] a,np.ndarray[np.float64_t, ndim=1] b,np.ndarray[np.float64_t, ndim=1] c,np.ndarray[np.float64_t, ndim=1] d):
    cdef np.ndarray[np.float64_t, ndim=1] cp = np.zeros(n,dtype=DTYPE)
    cdef np.ndarray[np.float64_t, ndim=1] dp = np.zeros(n,dtype=DTYPE)
    cdef np.ndarray[np.float64_t, ndim=1] v = np.zeros(n,dtype=DTYPE)
    cdef Py_ssize_t i,j,k
    
    for i in range(n-1):
        if i == 0:
            cp[i] = c[i]/b[i]
        else:
            j=i-1
            cp[i] = c[i]/(b[i] - a[i]*cp[j])
    for i in range(n):
        if i == 0:
            dp[i] = d[i]/b[i]
        else:
            j=i-1
            dp[i] = (d[i] - a[i]*dp[j])/(b[i]-a[i]*cp[j])
    for i in range(n):
        if i == 0:
            j=n-1-i
            v[j] = dp[j]
        else:
            j=n-1-i
            k=n-i
            v[j] = dp[j] - cp[j]*v[k]
    return v