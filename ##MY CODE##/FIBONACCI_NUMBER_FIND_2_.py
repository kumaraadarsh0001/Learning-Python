n=int(input("enter the no of digit"))
x=0
y=1
z=0
print('your fibonacci numbers is:')
for i in range(n):
    print(i,"=",z)
    z=x+y
    y=x
    x=z
#another fibonacci series same as upper
n=int(input("enter the  number where you want to stop the series "))
a=int(input("enter the first term"))
b=int(input("enter the second  term"))
print("first term is =",a)
print("second term is =",b)
for i in range(a,n):
    c=a+b
    a=b
    b=c
    print(c)