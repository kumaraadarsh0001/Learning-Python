stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek',104: 'JD'}
print('original dict:')
print('STU=',stu)
print()
all_keys=stu.keys()
print(all_keys)
print(type(all_keys))
print()
lst=list(all_keys)    #it can convert it into list form
print(type(lst))
print(lst[0])         #it can give value from 0 index 
for j in lst:
    print(j)