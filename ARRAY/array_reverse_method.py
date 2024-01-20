#reverse method
import array
stu_roll=array.array("i",[101,102,103,104,105,106])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after reverse")
stu_roll.reverse()
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1