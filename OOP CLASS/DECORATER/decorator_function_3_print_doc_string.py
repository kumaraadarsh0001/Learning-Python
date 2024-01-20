from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper

@print_function_data
def add(a,b):
    """this function takes two numbers as argument and return their sum"""
    return a+b

print(add(21,29))