a=int(input('enter your first number='))
b=int(input('enter your last number='))
i=int(input('enter number to devide by='))
j=int(input('enter 2nd number to devide by='))
while(a<=b):
    if a%i==0:
        if a%j==0:
            print(a)
    a+=1
