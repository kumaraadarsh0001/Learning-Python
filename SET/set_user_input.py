a=set()
print(id(a))
n=int(input('enter number of element='))
for i in range(n):
    el=input("enter your elements=")
    a.add(el)
print(a)
print(id(a))
for i in a:
    print(i)