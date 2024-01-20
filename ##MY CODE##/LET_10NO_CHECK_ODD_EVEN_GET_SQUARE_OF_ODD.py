x=[11,12,13,14,15,16,17,18,19,20]
n=len(x)
y=[]
z=[]
a=[]
n=len(x)
for i in range(n):
    if i%2==0:
        y.append(x[i])
        
    else:
        z.append(x[i])
print("X=",x)
print("ODD=",y)
print("EVEN=",z)
for j in y:
    a.append(j**2)
print("SQUARE=",a)