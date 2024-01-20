#slicing tuple
x=(101,102,103,104,105,106,107,108)
print('Original Tuple')
n=len(x)
for i in range(n):
    print(i,'=',x[i])
print()

print('from 1st potition to 4th potition')
a=x[1:5]
for i in a:
    print(i)
print()

print('from 0th potition to last potition')
a=x[0:]
for i in a:
    print(i)
print()

print('last 4 element')
a=x[-5:]
for i in a:
    print(i)
print()

print('from 0th potition to 6th potition with step of 2')
a=x[0:7:2]
for i in a:
    print(i)
print()

print('from -5th potition to -3rd potition')
a=x[-5:-3]
for i in a:
    print(i)
print()