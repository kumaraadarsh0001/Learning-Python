import array
stu_roll=array.array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    
print("array after append")
stu_roll.append(106)
stu_roll.append(107)
stu_roll.append(108)
stu_roll.append(109)
stu_roll.append(110)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1