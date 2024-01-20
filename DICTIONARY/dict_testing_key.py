#testing key return true or false to chek element in dictionary
stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek'}
x=101 in stu
a=101 not in stu
y=104 in stu
b=104 not in stu
print('101 in dictionary        =',x)           #it returns true 101 is exists
print('101 not in dictionary    =',a)           #it returns false 101 is not exists
print('104 in dictionary        =',y)           #it returns false 101 is not exists
print('104 not in dictionary    =',b)           #it returns true 101 is exists