import numpy as np

var=np.array([12,45,69,54,36,89])

reshape1=var.reshape(2,3)
reshape2=var.reshape(3,2)

print(reshape1)
print(reshape1.ndim)
print(reshape2)
print(reshape2.ndim)