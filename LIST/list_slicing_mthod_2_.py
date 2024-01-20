x=[101,102,103,104,105,106,107]
print("original list")
n=len(x)
for i in range(n):
    print(i,"=",x[i])
print()

print("from 0th potition to 6th position")
a=x[0:7:2]
for i in a:
    print(i)
print()

print("from 0th potision to last potion")
b=x[-4:-2]
for i in b:
    print(i)