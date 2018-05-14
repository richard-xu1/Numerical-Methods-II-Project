#Implements a linear time tridiagonal Gaussian elimination solver
import numpy as np
import scipy as sp
import parameters as par

n = par.n             #import number of spatial discretizations

def tridiagonalSolve(a,b,c,d):
    cp = np.zeros(n)
    v = np.zeros(n)
    for i in range(n-1):
        if i == 0:
            cp[i] = c[i]/b[i]
        else:
            cp[i] = c[i]/(b[i] - a[i]*cp[i-1])
    for i in range(n):
        if i == 0:
            dp[i] = d[i]/b[i]
        else:
            dp[i] = (d[i] - a[i]*dp[i-1])/(b[i]-a[i]*cp[i-1])
    for i in range(n):
        if i == 0:
            v[n-1-i] = dp[i]
        else:
            v[n-1-i] = dp[i] - cp[i]*v[n-i]
    return v