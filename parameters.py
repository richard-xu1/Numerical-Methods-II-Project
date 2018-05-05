#Computation of myelinated and unmyelenated axons
#This code specifies the parameters of the Linear Cable

caseNumber = #{Case #1: Unmyelenated , Case #2: Myelenated}

#For Case #2
numOfNor = 0                            #Number of Nodes of Ranvier excluding starting and end Nodes
mylSections = numOfNor + 1               #number of myelinated sections
nodeLen = 1                             # node of ranvier length in micrometers

n = mylSections*mylPoints + (numofNor + 2)*norPoints                       #Total points in Linear Cable 
norPoints = 10									#Node of Ranvier Grid Points
MylNorRatio = 148                               # Mylin length to Node length ratio
mylPoints = MylNorRatio*norPoints							#Myelin section Grid Points
dx = cableLength/n                #dx size in micrometers found by dividing total cable length by total number og grid points
cableLength = nodeLen*(numofNor + 2) + MylNorRatio*mylSections  #total Length of cable in micrometers
#Build Grid should create create arrays v[n],M[n], N[n], H[n] which store the value
#of voltage and gating variables at time t_k.

BuildGrid(caseNumber, numOfNor, mylSections, n, norPoints, mylPoints) 

#BuildCoefficients should return the values of a[n],b[n],c[n], which are the coefficients
#of voltage at time t_k+1 and are hence the entries in the tridiagonal system

BuildCoefficients(caseNumber, numOfNor, mylSections, n, norPoints, mylPoints)

#buildD should return the right hand side vector of the tridiagonal system
d = buildD()

time	= 
dt		= 
dx 		= 


tridiagonalSolve(a,b,c,d)
	

