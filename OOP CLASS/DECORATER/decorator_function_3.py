from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrrapper_func(*args,**kwargs):
        """this is wrapper function"""
        print("lovely boy badshah")
        return any_function(*args,**kwargs)
    return wrrapper_func
@decorator_function    #it will give all value of decore_func into func1
def func1():
    """this is add function"""
    print("KUMAR AADARSH")

print(func1.__doc__)
print(func1.__name__)