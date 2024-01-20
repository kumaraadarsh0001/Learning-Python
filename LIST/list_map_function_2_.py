#map function in list from lambda function
a=[10,20,30,40,50]
b=[1,2,3,4,5]

result=map(lambda n,m:n+m,a,b)
print(result)
print(type(result))
for i in result:
    print(i)