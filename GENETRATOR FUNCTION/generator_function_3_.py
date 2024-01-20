#generator function 
from unittest import result


x=int(input('enter your number='))
y=int(input('enter your number='))
z=int(input('enter your number='))
def show(a,b,c):    
    yield a       
    yield b
    yield c     
result=show(x,y,z)
print(result)
print(type(result))
print("***************")
print(next(result))
print(next(result))