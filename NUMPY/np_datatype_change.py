import numpy as np


print('\nOriginal data type :')
var=np.array([1,2,3,4,5])
print(var)
print('Data type :',var.dtype)
print()
varc=np.array([1,2,3,4,5],dtype="int16")
print(varc)
print('After change data type :')
print('Data type :',varc.dtype)