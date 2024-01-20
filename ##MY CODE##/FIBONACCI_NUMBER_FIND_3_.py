def func(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return func(n-1) + func(n-2)
x=int(input('enter your first number='))
y=int(input('enter your first number='))
for i in range(x,y+1):
    print(i,"=",func(i))