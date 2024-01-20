#list of tuples
a=(10,20,[30,40])
print("Original list A:",a)
print(id(a))
print(type(a))
print()
#Accesssing tuple of list usinh for loop
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])