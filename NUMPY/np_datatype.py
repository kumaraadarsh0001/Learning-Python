import numpy as np
print('For integer')
var=np.array([1,2,3,4,5])
print('Data type :',var.dtype)

print('\nFor float')
var1=np.array([1.23,2.32,3.0,4.5,12.0])
print('Data type :',var1.dtype)

print('\nFor string')
var2=np.array(['kumar','aadarsh','lovely','Badshah'])
print('Data type :',var2.dtype)

print('\nFor string and number')
var2=np.array([1,2,3,4,'kumar','aadarsh','lovely','Badshah'])
print('Data type :',var2.dtype)

print('\nFor string and float')
var2=np.array(['aadarsh','lovely','Badshah',1.23,2.32,3.0,4.5])
print('Data type :',var2.dtype)