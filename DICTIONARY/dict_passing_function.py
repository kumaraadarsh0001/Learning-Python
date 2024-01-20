#Passing Dictionary to function
def dict(x):
    print(x)
    print(type(x))
    for k in x:
        print(k,'=',x[k])
dc={101:'kumar aadarsh',102:'lovely boy',103:'flirting king'}
dict(dc)