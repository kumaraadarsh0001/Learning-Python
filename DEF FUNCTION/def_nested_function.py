#nested function
def name():
    def num():
        print("lovely boy badshah")
    print("kumar aadarsh")
    num()
name()


#nested def function
def disp(n):
    def show():
        return "show function "
    result=show()+n+" disp function"
    return result
a=disp("HERO")
print(a)