a=((10,20,30),(40,50,60))
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()