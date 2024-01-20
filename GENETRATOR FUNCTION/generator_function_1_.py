#generator function 
x=int(input('enter your number='))
y=int(input('enter your number='))
def show(a,b):    
    yield a       
    yield b     
p,q=show(x,y)
print(p,type(p))
print(q,type(q))
