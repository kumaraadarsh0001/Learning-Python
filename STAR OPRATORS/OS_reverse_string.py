def func(lst,**kwargs):
    if kwargs.get("reverse_str")==True:
        return[name[::-1].title() for name in lst]
    else:
        return[name.title() for name in lst]

names=["KUAMR","AADARSH"]
print(func(names))
print("After modification")
print(func(names,reverse_str=True))