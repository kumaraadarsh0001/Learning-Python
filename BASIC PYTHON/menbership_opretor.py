#membership opretor
a="LOVELYBOYBADSHAH"
b=[10,20,5,30.23]
c=(10,3,324,24,43.34)
d={20,10,30,50,40}
e={101:'aadarsh',102:'anish',103:'abhishek'}
print('string:')
print("LOVE" in a)
print("love" not in a)
print()
print('list:')
print(10 in b)
print(10 not in b)
print()
print('tuple:')
print(324 in b)
print(324 not in b)
print()
print('set:')
print(50 in c)
print(50 not in c)
print()
print('dictionary:')
print(101 in d)
print('anish' in d)#it gives false because it will find only key in dictionary
print(101 not in d)