#pass a function as parameter
def disp(n):
    print("disp function"+n())

def show():
    return " show functon"

disp(show)


#pass a function as parameter
def disp(n):
    return "disp function"+n()

def show():
    return " show functon"

disp(show)
print(disp(show))