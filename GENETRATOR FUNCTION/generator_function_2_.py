#generator function 
x=input('enter your number=')
y=input('enter your number=')
def show(a,b):    
    yield a       
    yield b     
result=show(x,y)
print(result)
print(type(result))
print('*********************')
lst=list(result)
print(lst)