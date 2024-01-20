stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek',104: 'JD'}
print('original dict:')
print('STU=',stu)
print('ID:',id(stu))
print()
print('after using items method:')
it=stu.items()      #it can use to get items from dict
print(it)
print(type(it))
print('ID:',id(it))
print()
lst=list(it)        #it can convert it into list form
print(type(lst))
print(id(lst))
print(lst[0])       #it can give value from 0 index 
for i in lst:
    for j in i:
        print(j)