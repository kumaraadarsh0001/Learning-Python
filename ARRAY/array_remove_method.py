#remove method in array
import array
stu_roll=array.array("i",[101,102,101,104,105,106])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after remove")
stu_roll.remove(101)
stu_roll.remove(106)

n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
