#extend() method
import array
stu_roll=array.array("i",[101,102,104,105,106])
arr=array.array('i',[107,108,109])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after insert")
stu_roll.extend(arr)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1