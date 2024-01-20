i=1
s=0
n=int(input('enter your no.'))
while i<=n:
    if(i%2==0):
        print(i)
        s+=i
    i+=1
print('sum',s)