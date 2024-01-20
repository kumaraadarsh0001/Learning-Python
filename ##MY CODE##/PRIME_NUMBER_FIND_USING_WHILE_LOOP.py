a=int(input('enter first number='))
b=int(input('enter the last number='))
while (a<=b):
    i=1
    j=0
    while(i<=a):
        if(a%i==0):
            j+=1
        i+=1
    if(j==2):
        print(a)
    a+=1