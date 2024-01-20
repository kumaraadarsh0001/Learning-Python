#insert method in array
import array
stu_roll=array.array("i",[101,103,105,106,107,108])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after insert")
stu_roll.insert(1,102)
stu_roll.insert(3,104)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1