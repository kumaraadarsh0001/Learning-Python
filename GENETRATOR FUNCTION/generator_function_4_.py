from re import I
from unittest import result


def show(x,y):
    while x<=y:
        yield x
        x+=1

result=show(1,10)
print(result)
print(type(result))
print("**************")
print(next(result))
print(next(result))
print("**************")
for i in result:
    print(i)