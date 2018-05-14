import main
import numpy as np

std1 = main.main(1)
std2 = main.main(2)
std4 = main.main(3)

conv = np.log2(np.divide(np.absolute(std4 - std2),np.absolute(std2 - std1))) 
print conv