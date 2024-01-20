stu={101: 'anish', 102: 'dilip', 103: 'abhishek',104:'jd',105:'aadarsh'}
print('original dictionary:')
print('STU=',stu)
print('ID =',id(stu))
print()
print('after using pop in dictionary:')
x=stu.popitem()            #it can only remove a element from last index
y=stu.popitem()            #it can only remove a element from last index
print('STU=',stu)
print('ID =',id(stu))
print('removed value=',x,y)