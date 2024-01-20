a=[10,20,30,40,[50,60,70,80]]
b=[ 50, 60, 70, 80]
print('A',a)
print("after modifying")
a[0]=111
a[1]=112
a[2]=113
a[3]=114
a[4][0]=115
a[4][1]=116
a[4][2]=117
a[4][3]=118
print(a)
for i in a:
    print(i)
print("rest of the code")