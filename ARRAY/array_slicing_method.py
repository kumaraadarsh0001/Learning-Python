#slicinig array
import array
stu_roll=array.array('i',[101,102,103,104,105,106,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])

print("*******************")
a=stu_roll[0:2]
for i in a:
    print(i)
print('rest of the code')



#slicing array 0 to last number 
import array
stu_roll=array.array('i',[101,102,103,104,105,106,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])

print("*******************")
a=stu_roll[0:5]
for i in a:
    print(i)
print('rest of the code')