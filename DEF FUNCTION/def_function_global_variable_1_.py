from re import X


a=10
def show():
    x=20
    y=a+x
    print(y)

show()
print("global variable=",a)
print("local variable=",x)