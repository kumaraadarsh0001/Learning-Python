print("list before pop")
a=[8,9,10,11,12,13,14]
for i in a:
    print(i)

print("list after pop")
n=a.pop()

for i in a:
    print(i)

print("removed element:",n)