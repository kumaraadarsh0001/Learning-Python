#check the number you have given is pelindrome or not 
x=input('enter  number=')
y=x[::-1]
if (x==y):
    print(x,"=",y)
    print("yes it is pelendrome number")
else:
    print('it is not pelindrome')