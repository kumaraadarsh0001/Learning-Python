#passing tuple to function
def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t
tup=(10,20,30,"kumar aadarsh")
new_tup=show(tup)