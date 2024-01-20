#returning array from def function 
from array import*

def show(ar):
    print("passed array ar:",ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar

a=array('i',[101,102,103,104,105])
y=show(a)
print("returning array Y:",y)
print(type(y))
for i in y:
    print(i)
