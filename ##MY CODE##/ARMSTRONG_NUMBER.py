from copy import copy


n=int(input("enter your number="))
sum=0
order=len(str(n))
x=copy(n)
while n>0:
    digit=n%10
    sum +=digit**order
    n=n//10
if(sum==x):
    print("yes this is an armstrong number")
else:
    print("no it is not an armstrong number") 