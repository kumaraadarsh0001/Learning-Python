#list of tuples
a=(10,20,[30,40])
print("Original list A:",a)
print(id(a))
print(type(a))
print()
#Modifying a new tuple
a[2][0]=90
print("After appending: ",a)
print(id(a))
print(type(a))