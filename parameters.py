#Computation of myelinated and unmyelenated axons
#This code specifies the parameters of the Linear Cable

caseNumber = 1 #{Case #1: Unmyelenated , Case #2: Myelenated}

#For Case #2
numOfNor = 1                            #Number of Nodes of Ranvier excluding starting and end Nodes
mylSections = numOfNor + 1               #number of myelinated sections
nodeLen = .0001                             # node of ranvier length in cm
myelinLen = 1.                               #length of myelinated section in cm

norPoints = 10									         #Node of Ranvier Grid Points
MylNorRatio = myelinLen/nodeLen                              # Myelin length to Node length ratio
mylPoints = 100							# Myelin section Grid Points
n = mylSections*mylPoints + (numOfNor + 2)*norPoints                       #Total points in Linear Cable 
cableLength = nodeLen*(numOfNor + 2) + MylNorRatio*mylSections  #total Length of cable in cm
dxa = nodeLen/norPoints                #dxa grid size on active cable
dxp = myelinLen/mylPoints              #dxp grid size on passive cable

#Physical Parameters
ra = 0.001			  # active cable radius in cm
rp = 0.001           #passive cable radius in cm
rhoA = 35.4			  # active axoplasmic resistivity Ohm*cm
rhoP = 35.4            # passive axoplasmic resistivity  Ohm*cm
CN = 1			  # nodal membrane capacitance in microfarads/cm^2
gNA = 120                # active sodium gating constant   
gK = 36                  # active potassium gating constant 
gL = 0.3                     # active leakage gating constant
ratio=0.0001
CM = 0.001*CN			  # myelinated membrane capacitance in microfards/cm^2
gNAp = ratio*gNA              #passive sodium gating constant
gKp = ratio*gK                #passive potassium gating constant
gLp = gL                #passive leakage gating constant
ENA = 45                # mV
EK = -82                # mV
EL = -59                # mV
v_rest = -70            # mV
ELP= -70

T=1     
dt=.00001
tsteps=int (T/dt)


#Parameters for Injected Current
t1 = 0.01
t2 = 0.02
i0 = 0.03          
#Build Grid should create create arrays v[n],M[n], N[n], H[n] which store the value
#of voltage and gating variables at time t_k.

def injectedCurrent(t):
    if t < t1:
       return 0
    elif t > t1 and t < t2:
       return i0
    else: 
        return 0

#grid is a bit string that describes nature of point
# 0: active cable internal, 1: passive internal, 2: active to passive
# 3: passive to active, 4: start point, 5: end point
grid = [0]*n
# print grid
if (caseNumber == 0):
    for i in range (0,n):
        grid[i] = 0
    grid[0] = 4
    grid[n-1] = 5
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
