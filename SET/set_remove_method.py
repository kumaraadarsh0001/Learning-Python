a={'Lovely', 10, 12.12, 4560, 'Boy', 'python', 985}
print('before discarding',id(a))
a.remove('python')
print(a)        #it will print successfuly
print('after discarding',id(a))
a.remove('aadarsh')  #but this give an error because there are no element ('aadarsh)