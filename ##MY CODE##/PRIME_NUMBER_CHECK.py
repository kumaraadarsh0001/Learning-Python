n=int(input('enter number'))
a=0
i=1
while(i<=n):
    if(n%i==0):
        a+=1
    i+=1
if(a==2):
    print('prime number')
else:
    print("composite number")