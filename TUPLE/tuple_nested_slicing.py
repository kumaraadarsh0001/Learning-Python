x=((10,20,30),
   (40,50,60),
   (70,80,90),
   (11,22,33),
   (44,55,66),
   (77,88,99),
   (12,13,14))
print("original list")
for i in x:
    print(i)
print()
print("from 1st position to 4th position")
a=x[1:5] 
for j in a:
    print(j)
print()
print("from 0st position to last position")
a=x[0:]
for k in a:
    print(k)
print()
print("from last 5 lists with [-5(-3)]=2 lists towards right")
a=x[-5:-3]
for j in a:
    print(j)