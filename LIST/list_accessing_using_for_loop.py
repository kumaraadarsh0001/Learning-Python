print("without index accessing list using for loop")
a=[11,12,13,14,14,543,64,56,12,13,53]
for i in a:
    print(i)



print("accessing list using for loop with index")
a=[11,12,13,14,14,543,64,56,12,13,53]
n=len(a)
for i in range(n):
    print(i,"=",a[i])