#Computation of myelinated and unmyelenated axons
#This code specifies the parameters of the Linear Cable
import numpy as np
caseNumber = 1 #{Case #1: Unmyelenated , Case #2: Myelenated}

#For Case #2
numOfNor = 10                           # Number of Nodes of Ranvier excluding starting and end Nodes
if caseNumber == 0:
    numOfNor = 0
mylSections = numOfNor + 1              # number of myelinated sections

if caseNumber == 1:
    norPoints = 10
    nodeLen = .002                         # node of ranvier length in cm
    myelinLen = 1.                          # length of myelinated section in cm
else:
    norPoints = 200
    nodeLen = 5.
    myelinLen = .5                            #length of myelinated section in cm

									         #Node of Ranvier Grid Points
mylPoints = 100							# Myelin section Grid Points
n = mylSections*mylPoints + (numOfNor + 2)*norPoints                       #Total points in Linear Cable 
cableLength = nodeLen*(numOfNor + 2) + myelinLen*mylSections  #total Length of cable in cm
dxa = nodeLen/norPoints                #dxa grid size on active cable
dxp = myelinLen/mylPoints              #dxp grid size on passive cable

#Physical Parameters
ra = 0.005			  # active cable radius in cm
rp = 0.007           #passive cable radius in cm
rhoA = 0.0354		  # active axoplasmic resistivity Ohm*cm
rhoP = 0.0354            # passive axoplasmic resistivity  Ohm*cm
CN = 1			  # nodal membrane capacitance in microfarads/cm^2
if caseNumber == 1:
    gNA = 2400             # active sodium gating constant 
    gK = 400               # active potassium gating constant 36    
else:
    gNA = 120
    gK = 36 
gL = 0.3                     # active leakage gating constant
gratio=0.004
cratio= 0.004
CM = cratio*CN			  # myelinated membrane capacitance in microfards/cm^2
CJ = (CM*2.*np.pi*rp*dxp)/2 + (CN*2.*np.pi*ra*dxa)/2
gNAp = 0              #passive sodium gating constant
gKp = 0                #passive potassium gating constant
gLp = gratio*gL                #passive leakage gating constant
ENA = 45                # mV
EK = -82                # mV
EL = -59                # mV
v_rest = -70            # mV
ELP= -70

T = 6     
Tf=T/100.
dt=.002
tsteps=int (T/dt)


#Parameters for Injected Current
t1 = 0.01
t2 = 0.02
i0 = 30          
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
grid = np.zeros(n)
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