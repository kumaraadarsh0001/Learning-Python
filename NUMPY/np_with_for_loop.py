import numpy as np

l=[]
n=int(input("Enter range of list"))
for i in range(n):
    element=int(input("enter element :"))
    l.append(element)

print(np.array(l))