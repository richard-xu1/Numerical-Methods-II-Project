#Computation of myelinated and unmyelenated axons
#This code specifies the parameters of the Linear Cable

caseNumber = #{Case #1: Unmyelenated , Case #2: Myelenated}

#For Case #2
numOfNor = 0                            #Number of Nodes of Ranvier excluding starting and end Nodes
mylSections = numOfNor + 1               #number of myelinated sections
nodeLen = .001                             # node of ranvier length in millimeter

norPoints = 10									#Node of Ranvier Grid Points
MylNorRatio = 148                               # Myelin length to Node length ratio
mylPoints = MylNorRatio*norPoints							#Myelin section Grid Points
n = mylSections*mylPoints + (numOfNor + 2)*norPoints                       #Total points in Linear Cable 
cableLength = nodeLen*(numOfNor + 2) + MylNorRatio*mylSections  #total Length of cable in millimeter
dx = cableLength/n                #dx size in millimeter found by dividing total cable length by total number og grid points
r = 0.0005			  #cable radius in millimeters
rho = 354			  # axoplasmic resistivity Ohm*mm
CN = 1.5			  # nodal membrane capacitance in micromicrofarads
CM = 1.6			  # myelinated membrane capacitance in micromicrofarads
Tmata = -r/(4*rho*dx*dx)          # factor in front of v_{j-1} in our tridiagonal operator
Tmatb = CN/dt + r/(2*rho*dx*dx)   # factor in front of v_j in our tridiagonal operator
Tmatc = -r/(4*rho*dx*dx)	  # factor in front of v_{j+1} in our tridiagonal operator

#Build Grid should create create arrays v[n],M[n], N[n], H[n] which store the value
#of voltage and gating variables at time t_k.

#grid is a bit string that describes whether a point is myelinated or unmyelinated
grid = [False]*n
# print grid
if (caseNumber == 0):
    for i in range (0,n):
        grid[i] = False
else: 
    for j in range(0,numOfNor+1):
        print "j is" + str(j)
        norStartIndex = j*(norPoints+mylPoints)
        mylStartIndex = norStartIndex +norPoints
        print "NOR Start Index is"+str(norStartIndex)
        print "mylStartIndex is"+str(mylStartIndex)
        print "norPoints is" +str(norPoints)
        for i in range(norStartIndex,norStartIndex+norPoints):
            print "i is" + str(i)
            grid[i] = False
        for m in range(mylStartIndex,mylStartIndex+mylPoints):
            print "m is" + str(m)
            grid[m] = True
    for i in range(n-norPoints,n-1):
        grid[i] = False
# print grid 

#BuildCoefficients should return the values of a[n],b[n],c[n], which are the coefficients
#of voltage at time t_k+1 and are hence the entries in the tridiagonal system

BuildCoefficients(caseNumber, numOfNor, mylSections, n, norPoints, mylPoints)





	

