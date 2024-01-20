def decorator_function(any_function):
    def wrrapper_func(*args,**kwargs):  #*args,**kwargs it will give permition to give value for parameter
        print("lovely boy badshah")
        return any_function(*args,**kwargs)
    return wrrapper_func
@decorator_function    #it will give all value of decore_func into func1
def func1(a):
    print(f"KUMAR AADARSH {a}")
func1(420)
print()
@decorator_function    #it will give all value of decore_func into func2
def func2(a,b):
    return a+b
print(func2(12,12))