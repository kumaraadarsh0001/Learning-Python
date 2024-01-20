x=[11,22,33,44,55,66,77,88,99,10]
y=[]
z=[]
a=[]
b=[]
n=len(x)
for i in range(n):
    if i%2==0:
        y.append(i)
    else:
        z.append(x[i]**2)
        a.append(i)
        b.append(x[i])
y.clear()
print("LIST=",x)
print("REMOVED EVEN INDEX(ELEMENT)   =   ",y)
print("ODD INDEX IN LIST             =   ",a)
print("ELEMENT ON ODD INDEX IN LIST  =   ",b)
print("SQUARE OF ODD INDEX(ELEMENT)  =   ",z)