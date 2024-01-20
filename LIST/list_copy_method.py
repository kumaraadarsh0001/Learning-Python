print("copying a list")
a=[10,20,30,40,50,60]
b=a.copy()
print("id of a=", id(a))
print("id of b=",id(b))
print()
print("A:",a)
print("B:",b)     
print()
print("modifying A:")
a[1]=55
print("A:",a)
print("B:",b)
print()
print("modifyinng B:")
b[0]=66
print("A:",a)
print("B:",b)