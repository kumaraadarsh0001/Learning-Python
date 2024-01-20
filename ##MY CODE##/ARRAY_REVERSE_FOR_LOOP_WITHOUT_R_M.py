import array
stu_roll=array.array('i',[11,25,23,44,55,68,744,800])
n=len(stu_roll)
for i in range(n-1,-1,-1):
    print(stu_roll[i])