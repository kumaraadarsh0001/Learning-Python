print("accessing list using while loop with index")
a=[11,12,13,14,14,543,64,56,12,13,53]
n=len(a)
i=0
while i<n:
    print(i,"=",a[i])
    i+=1

print("without index accessing list using while loop")
a=[11,12,13,14,14,543,64,56,12,13,53]
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1