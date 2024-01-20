#tuple is not modify because thier element are inmutable
print("this is not modifying method like example(a[0]=12)")
a=(10,20,30,70,80,90)
print("A:",a)
x=(40,50,60)
print("X:",x)
print("after breaking tuple A:")
y=a[0:3]
print("A1",y)
z=a[3:]
print("A2",z)
print("after adding A1 , X , A2 then")
b=y+x+z
print("result:",b)