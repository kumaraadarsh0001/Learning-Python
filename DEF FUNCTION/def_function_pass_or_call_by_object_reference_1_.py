def show(x):
    print(x,id(x))
    x=15
    print(x,id(x))

x=10
show(x)
print(x,id(x))