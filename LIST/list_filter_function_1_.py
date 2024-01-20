age=[19,5,22,7,30,9,45,12,15,17,2]
def func(x):
    if x<15:
        return False
    else:
        return True

adults=list(filter(func,age))
print(age)
print(adults)
print(type(adults))

for j in adults:
    print(j)