a={'Lovely', 10, 12.12, 4560, 'Boy', 'aadarsh', 985}
b={'Lovely', 'kumar', 'Boy', 'python','aadarsh'}
print(a)
print(id(a))
print(b)
print(id(b))
um=a.union(b)
print(um)     #It will give to the elements of both the sets but only once to the ones that are there.
print(id(um))