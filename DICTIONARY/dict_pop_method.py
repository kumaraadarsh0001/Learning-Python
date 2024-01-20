stu={101: 'anish', 102: 'dilip', 103: 'abhishek',104:'jd',105:'aadarsh'}
print('original dictionary:')
print('STU=',stu)
print('ID =',id(stu))
print()
print('after using pop in dictionary:')
stu.pop(105)                               #it can remove a element from 105 index
print(stu.pop(106,'not found key'))        #if index not found it can return default value
print('STU=',stu)
print('ID =',id(stu))