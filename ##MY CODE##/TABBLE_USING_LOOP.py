a=int(input('enter the number='))
b=1
i=0
while b<=10:
    print(a,'*',b,"=",a*b) 
    i+=a*b
    b+=1
print()
print("SUM OF ALL=",i)
print()
for j in range(10,0,-1):
    print(a,"*",j,"=",a*j)