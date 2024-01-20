from array import*
stu_roll=array("i",[])
n=int(input("how many elements?"))

for i in range(n):
    stu_roll.append(int(input("enter elements")))

for i in range(len(stu_roll)):
    print(stu_roll[i])