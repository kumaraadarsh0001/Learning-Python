stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek'}
print('original dict:')
print('STU=',stu)
print('ID:',id(stu))
new=stu.get(101)
new2=stu.get(104,'lovely boy')    #if you can't give default value it will print NONE 
print('after using get method:')
print('NEW   =',new)        #it can return the value of entered key
print('NEW2  =',new2)       #it can retuns default value because entered key is not exists