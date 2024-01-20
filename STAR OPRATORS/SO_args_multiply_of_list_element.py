#*args with normal parameter
def multiply_nums(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
num=[5,2,3,4,3,5,9]
print(multiply_nums(*num))#if you give star at first from list name it will unpack your list
print(multiply_nums(num))#if you not give star at first from list name it will gives you same as list