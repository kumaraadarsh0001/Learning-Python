def show(x):
    print('SET OF X:\n',x)
    print("ID of X:\n",id(x))
    for i in x:
        print(i)
    return x
a={'lovely',232,'boy','badshah',321.223}
new_set=show(a)
print('SET OF NEW_SET:\n',new_set)
print("ID of NEW_SET:\n",id(new_set))