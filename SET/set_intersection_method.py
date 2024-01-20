a={'Lovely', 10, 12.12, 4560, 'Boy', 'aadarsh', 985}
b={'Lovely', 'kumar', 'Boy', 'python','aadarsh'}
print(a)
print(id(a))
print(b)
print(id(b))
ism=a.intersection(b)    #This will give only those elements which are in the two sets
print(ism)
print(id(ism))