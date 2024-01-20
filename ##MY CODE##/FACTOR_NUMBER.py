a=int(input("enter the number ="))
b=1
n=1
if b<=a:
    while(b<=a):
        n=n*b
        b+=1
    print(f"factorial of {a} is=",n)
elif(a==0):
    print(f"factorial of {a} is=",n)
elif(a<=-1):
    print("not define for negative numbers")