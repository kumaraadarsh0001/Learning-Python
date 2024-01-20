#nested tuple using for loop
a=((10,20,30),(40,50,60))
#without index
for i in a:
    for j in i:
        print(j)
    print()