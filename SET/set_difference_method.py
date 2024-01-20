a={'Lovely', 10, 12.12, 4560, 'Boy', 'aadarsh', 985}
b={'Lovely', 'kumar', 'Boy', 'python','aadarsh'}
print(a)
print(id(a))
print(b)
print(id(b))
dm=a.difference(b)    #It will only give a different elemnet from set A
print(dm)
print(id(dm))