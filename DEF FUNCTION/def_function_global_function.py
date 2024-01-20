a=20
def show():
    a=10
    print("local veriable=",a)
    x= globals()["a"]
    print("X=",x)
show()
print("global veriable=",a)