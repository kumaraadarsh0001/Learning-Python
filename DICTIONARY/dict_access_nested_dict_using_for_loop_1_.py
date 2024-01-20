#Accessing Nested dictionary using for loop
a={'course':'Python','fees':72990,1:{'course':'Java Script','fees':72990}}
#Accessing each id keys --values
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k,'=',a[i][k])
    else:
        print(i,'=',a[i])