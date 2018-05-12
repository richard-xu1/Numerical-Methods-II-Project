#Computation of myelinated and unmyelenated axons
#This code specifies the parameters of the Linear Cable

caseNumber = 1 #{Case #1: Unmyelenated , Case #2: Myelenated}

#For Case #2
numOfNor = 0                            #Number of Nodes of Ranvier excluding starting and end Nodes
mylSections = numOfNor + 1               #number of myelinated sections
nodeLen = .001                             # node of ranvier length in millimeter
myelinLen = 1                               #length of myelinated section in millimeter

norPoints = 10									         #Node of Ranvier Grid Points
MylNorRatio = myelinLen/nodeLen                              # Myelin length to Node length ratio
mylPoints = 100							# Myelin section Grid Points
n = mylSections*mylPoints + (numOfNor + 2)*norPoints                       #Total points in Linear Cable 
cableLength = nodeLen*(numOfNor + 2) + MylNorRatio*mylSections  #total Length of cable in millimeter
dxa = nodeLen/norLength                #dxa grid size on active cable
dxp = myelinLen/mylPoints              #dxp grid size on passive cable

ra = 0.0005			  # active cable radius in millimeters
rp = 0.0005             #passive cable radius in millimeters
rhoA = 35.4			  # active axoplasmic resistivity Ohm*cm
rhoP = 35.4            # passive axoplasmic resistivity  Ohm*cm
CN = 1.5			  # nodal membrane capacitance in micromicrofarads
CM = 1.6			  # myelinated membrane capacitance in micromicrofarads
gNA = 120                # sodium gating constant   
gK = 36                  #potassium gating constant 
gL = 0.3                     #L gating constant 
T=1     
r1= 1
r2= 14               
dt=dx*dx
#Build Grid should create create arrays v[n],M[n], N[n], H[n] which store the value
#of voltage and gating variables at time t_k.

#grid is a bit string that describes nature of point
# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
grid = [0]*n
# print grid
if (caseNumber == 0):
    for i in range (0,n):
        grid[i] = 0
else: 
    for j in range(0,numOfNor+1):
        # print "j is" + str(j)
        norStartIndex = j*(norPoints+mylPoints)
        mylStartIndex = norStartIndex +norPoints
        # print "NOR Start Index is"+str(norStartIndex)
        # print "mylStartIndex is"+str(mylStartIndex)
        # print "norPoints is" +str(norPoints)
        for i in range(norStartIndex,norStartIndex+norPoints):
            # print "i is" + str(i)
            grid[i] = 0
        for m in range(mylStartIndex+1,mylStartIndex+mylPoints-1):
            # print "m is" + str(m)
            grid[m] = 1
        grid[mylStartIndex] = 2
        grid[mylStartIndex+mylPoints-1] = 3
    for i in range(n-norPoints,n-1):
        grid[i] =0
    grid[0] = 4
    grid[n-1] = 5
print grid
