from array import*
stu_roll=array("i",[])
n=int(input("enter number of element="))
i=0
j=0
while i<n:
    stu_roll.append(int(input("enter elements=")))
    i+=1

while (j<len(stu_roll)):
    print(stu_roll[j])
    j+=1