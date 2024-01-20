a=[]
n=int(input('enter your element='))

for i in range(n):
    a.append(int(input('enter your elements=')))

#You can make a tuple by appending the list and giving it another name.

print("A:",a)                           #A is list bfore append
print("TYPE OF A:",type(a))
print("ID:",id(a))
x=tuple(a)                              #X is tuple after append 
print("X:",x)
print("TYPE OF X:",type(x))             #A is list after append yoou cannot change tuple 
print("ID:",id(x))
print("A:",a)
print("TYPE OF A:",type(a))
print("ID:",id(a))