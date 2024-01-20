x=int(input("enter the start no.              ="))
y=int(input("enter the last no.               ="))
c=int(input("number by which to divide        ="))
z=[]
while x<=y:
    if x%c==0:
        z.append(x)
    x+=1
print(z)
n=len(z)        #find greater number in the list
a=z[0]
for i in range(n):
    if (z[i]>a):
        a=z[i]
print("max number=",a)
n=len(z)        #find smaller number in the list
b=z[0]
for i in range(n):
    if (z[i]<b):
        b=z[i]
print("min number=",b)