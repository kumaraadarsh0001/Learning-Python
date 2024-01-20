#list of tuples
a=[10,20,(30,40)]
print("Original list A:",a)
print(id(a))
print(type(a))
print()
#Appending a new tuple
a.append((50,60))
print("After appending: ",a)
print(id(a))
print(type(a))