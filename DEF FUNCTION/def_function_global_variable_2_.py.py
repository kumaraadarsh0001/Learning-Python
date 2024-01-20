#type error local variable in def function
a=0   #global variable
def show(b):
    a=a+b #local statement cannot ecept same variable without reference
    print(a)

show(12)


#local variable in def function same as global variable
a=0   #global variable
def show(b):
    a=1  #local variable
    a=a+b
    print(a)

show(12)
