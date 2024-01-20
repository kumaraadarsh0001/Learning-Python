#funcion retirn another function
def disp():
    def show():
        return "kumar aadarsh"
    print("disp function")
    return show

r_sh=disp()
print(r_sh())

#funcion retirn another function with parameter
def disp(sh):
    print("disp function")
    return sh

def show():
    return "show function"

a=disp(show)
print(a())

