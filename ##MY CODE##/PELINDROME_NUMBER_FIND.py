x=int(input('enter your first no  ='))
y=int(input('enter your last no   ='))
for i in range(x,y):
    n=i
    while  n>0:
     z=n%10
     y=y*10+z
     n=int(n/10)
    if i==y:
         print(i)
    y=0