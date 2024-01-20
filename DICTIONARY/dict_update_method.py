stu={101: 'anish', 102: 'dilip', 103: 'abhishek'}
print('original dictionary:')
print('STU=',stu)
print('ID=',id(stu))
print()
print('updated dictionary:')
val={'name':'aadarsh','address':'hisar',104:'aashish'}
stu.update(val)     #it can add anoter dict to original dict
print('STU=',stu)
print('ID=',id(stu))