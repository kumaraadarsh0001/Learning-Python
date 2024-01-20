x=[101,102,103,104,105,106,107]
print("original list")
n=len(x)
for i in range(n):
    print(i,"=",x[i])
print()

print("from 1st potition to 4th position")
a=x[1:5]
for i in a:
    print(i)
print()

print("from 0th potision to last potion")
b=x[0:]
for i in b:
    print(i)