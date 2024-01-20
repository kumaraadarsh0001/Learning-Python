a=[]
size=int(input("enter size of the list="))
for i in range(size):
    val=int(input("enter numbers="))
    a.append(val)
min=a[0]
for i in range(size):
    if (a[i]<min):
        min=a[i]
print("max number=",min)