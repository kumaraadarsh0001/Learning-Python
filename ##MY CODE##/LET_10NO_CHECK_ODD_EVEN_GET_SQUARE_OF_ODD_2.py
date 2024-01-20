x=[11,22,33,44,55,66,77,88,99,10]
y=[]
z=[]
a=[]
b=[]
c=[]
n=len(x)
for i in range(n):
    if i%2==0:
        y.append(i)
    else:
        z.append(i)
del y
print("X=",x)
print("ODD INDEX=",z)
n=len(x)
for j in range(n):
    if (x[j]%2==0):
        a.append(x[j]) 
    else:
        b.append(x[j])
del a
m=len(b)
for i in range(m):
    c.append(x[i]**2)
print("ODD No.:",b)
print("SQUARE=",c)