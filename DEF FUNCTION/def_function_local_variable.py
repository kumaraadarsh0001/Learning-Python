#local vriable 
def show():
    x="kumar aadarsh"
    print(x)

show()

#local variable =  Cannot print local variable at last of the statement
def show(y):
    x=20
    print(x+y)

show(12)
#print(x+y)  #it will give an error because local variable can't perform outer the function