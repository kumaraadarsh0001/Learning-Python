import numpy as np

var=np.array([1,2,3,4,5,6])
var1=np.float32(var)#it will change var into float data type
var2=np.int_(var1)#it will change var1 into integer data type
#it will print all values data type
print('Data Type :',var.dtype)
print('Data Type :',var1.dtype)
print('Data Type :',var2.dtype)
#it will print all values
print(var)
print(var1)
print(var2)