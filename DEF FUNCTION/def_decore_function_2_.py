#decorator function 
def name(func):
    def inner():
        a=func()
        add=a+5
        print("kumar")
        print("aadarsh")
        return add
    return inner 

def num():
    return 10
result=name(num)
print(result())