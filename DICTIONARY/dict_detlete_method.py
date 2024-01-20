#deleteing element in dictionary
stu={101: 'aadarsh', 102: 'dilip', 103: 'abhishek', 105: 'aashish', 104: 'anish'}
print('before deleteing:')
print(stu)
print(id(stu))
del stu[105]
del stu[104]
print('after deleteing:')
print(stu)
print(id(stu))
del stu
print(stu)  #it will give an error(stu is not define ) because stu is deleted 