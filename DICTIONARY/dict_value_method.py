stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek',104: 'JD'}
print('original dict:')
print('STU=',stu)
print()
all_values=stu.values()
print(all_values)
print(type(all_values))
print()
lst=list(all_values)    #it can convert it into list form
print(type(lst))
print(lst[0])           #it can give value from 0 index 
for j in lst:
    print(j)