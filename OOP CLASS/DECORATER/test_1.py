num=int(input("enter your number :"))
def decor_func1(any_func):
    def wrrapper_func():
        if num%2==0:
            any_func()
    return wrrapper_func
def decor_func2(any_func):
    def wrrapper_func():
        if num%3==0:
            any_func()
    return wrrapper_func
def decor_func3(any_func):
    def wrrapper_func():
        if num%5==0:
            any_func()
    return wrrapper_func
@decor_func1
@decor_func2
@decor_func3
def divide():
    print(num)
divide()