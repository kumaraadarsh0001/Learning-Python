#slicing tuple
x=(101,102,103,104,105,106,107,108)
print('Original Tuple')
n=len(x)
for i in range(n):
    print(i,'=',x[i])
print()

print('from 1st potition to 4th potition')
a=x[1:5]
print(a)
print()

print('from 0th potition to last potition')
b=x[0:]
print(b)
print()

print('last 4 element')
c=x[-5:]
print(c)
print()

print('from 0th potition to 6th potition with step of 2')
d=x[0:7:2]
print(d)
print()

print('from -5th potition to -3rd potition')
e=x[-5:-3]
print(e)
print()