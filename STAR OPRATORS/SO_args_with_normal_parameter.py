#*args with normal parameter
def multiply_nums(num,*args):
    multiply=1
    print(num)    #it will print onlhy num value 
    print(args)   #it will print a tuple of all value givan for parameter
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(5,2,3,4)) #here first value give to num(parameter)
#it will start multiply by second number