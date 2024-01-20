def show(l):
    print(l)
    print("***********************************")
    print(type(l))
    print("***********************************")
    for i in l:
        print(i)
    return l
lst=[10,20.3,30,5.08,"kumar aadarsh"]
new_lst=show(lst)
print("***********************************")
print("returnig list function :")
print(new_lst)
print("***********************************")
print("returnig type of function :")
print(type(new_lst))
print("***********************************")
print("rest of the code")