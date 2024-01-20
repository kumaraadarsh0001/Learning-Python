def decor_func(any_func):
    def wrrapper_func():
        print("lovely boy badshah")
        any_func()
    return wrrapper_func

def func1():
    print("KUMAR AADARSH")
def func2():
    print("AADARSH KUMAR")

var=decor_func(func1)
var()