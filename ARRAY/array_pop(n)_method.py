#pop(potition number) method in array
import array
stu_roll=array.array("i",[101,102,103,104,105,106])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after pop(n)")
r=stu_roll.pop(0)
s=stu_roll.pop(0)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
print("removed element",r,s)