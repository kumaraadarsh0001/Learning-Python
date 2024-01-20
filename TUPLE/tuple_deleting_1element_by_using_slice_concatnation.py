a=(10,20,-50,30,"kumar","aadarsh")
print("A:",a)
print(id(a))
t1=a[0:2]           #slicing element
t2=a[3:]            #slicing element
tpl=t1+t2           #using concatnation of slicing element
print("after deleting 1 element=(-50) from tuple:")
print(tpl)
print(id(tpl))
