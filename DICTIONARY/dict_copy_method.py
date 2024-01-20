#clear method is used to clear the dictionary
stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek'}
print('before copying dict:')
print('STU=',stu)
print('ID:',id(stu))
new=stu.copy()
print('after copying dict:')
print('NEW=',new)
print('ID:',id(new))
stu[101]='aadi'       #it can modify only stu dict not new 
print(stu)
print(new)