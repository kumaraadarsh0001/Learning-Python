print("list before remove")
a=[11,12,13,14,15,16]
for i in a:
    print(i)

print("list after remove")
a.remove(14)
a.remove(11)
for i in a:
    print(i)