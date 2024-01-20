#copying tuple
a=(10,20,30,40,50)
b=a
print("A:",a)
print("B:",b)
print("ID OF A:",id(a))
print("ID OF B:",id(b))
print()
a=b[1:5]
print("A:",a)
print("B:",b)
print("ID OF A:",id(a))
print("ID OF B:",id(b))