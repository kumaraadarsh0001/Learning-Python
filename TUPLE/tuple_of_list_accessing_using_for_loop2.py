#list of tuples
a=([10,20],[30,40])
print("Original list A:",a)
print(id(a))
print()
#Accessing tuple of lists using for loop
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()