#getting input from users for loop
import array
stu_roll=array.array('i',[])
n=int(input("enter nuber of elements"))

for i in range(n):
    stu_roll.append(int(input("enter element: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])