import main_conv_std
import numpy as np

std1,timestamp1 = main_conv_std.main(1)
std2,timestamp2 = main_conv_std.main(2)
std4,timestamp4 = main_conv_std.main(3)


conv = np.log2(np.divide(np.absolute(std4 - std2),np.absolute(std2 - std1))) 
print conv
print std1
print std2
print std4
print timestamp1
print timestamp2
print timestamp4
print conv.shape[0]
for i in range(timestamp4.shape[0]):
	print timestamp4[i]
for j in range(conv.shape[0]):
	print conv[j]