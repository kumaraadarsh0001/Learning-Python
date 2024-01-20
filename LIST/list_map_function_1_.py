#map function in list fron def function
a=[10,20,30,40,50]
def func(n):
    return n+5

result=list(map(func,a))
print(result)
print(type(result))
for i in result:
    print(i)

#map function in list from lambda function

a=[10,20,30,40,50]

result=map(lambda x:(x+2),a)
print(result)
print(type(result))
for i in result:
    print(i)