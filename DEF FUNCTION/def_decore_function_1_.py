def decor(num):
    def inner():
        print("before enhancing function")
        num()
        print("after enhancing function")
    return inner  
@decor
def num():
    print("we will use this function")
    print("and will enhance this in decorator")
num()