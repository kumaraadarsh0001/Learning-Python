from operator import truediv


i=1
while i<=3:
    print('outer loop',i)
    i+=1
    j=1
    while j<=5:
        print('inner loop',j)
        j+=1
print('rest of the code')
#neasted while loop
i=0
while True:
    i+=1
    print(i)
    if(i==10):
        break
print('rest of the code')
