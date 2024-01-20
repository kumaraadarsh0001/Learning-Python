age=[19,50,22,7,30,9,45,12,15,17,2]

adults=list(filter(lambda n: (n>=18),age))
print(adults)
print(type(adults))
print()
for j in adults:
    print(j)