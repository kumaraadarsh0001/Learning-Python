def decorator_function(any_func):
    def wrrapper_func():
        print("lovely boy badshah")
        any_func()
    return wrrapper_func
@decorator_function    #it will give all value of decore_func into func1
def func1():
    print("KUMAR AADARSH")
func1()
print()
@decorator_function    #it will give all value of decore_func into func2
def func2():
    print("AADARSH KUMAR")
func2()