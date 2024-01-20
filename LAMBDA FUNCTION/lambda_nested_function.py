add=lambda x=10:(lambda y: x+y)
x=int(input("enter x value="))
a=add(x)
print(a(45))