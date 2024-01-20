print("list before extend")
a=[11,12,13,14]
for i in a:
    print(i)

print("list after extend")
n=[15,16,17,18,19]
a.extend(n)
for i in a:
    print(i)

