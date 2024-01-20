print("list before insert")
a=[11,12,13,14]
for i in a:
    print(i)

print("list after insert")
a.insert(0,10)
a.insert(5,15)
for i in a:
    print(i)