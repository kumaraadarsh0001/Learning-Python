def decore1(num):
    def inner():
        b=num()
        multi=b*5
        return multi
    return inner
def decore(num):
    def inner():
        a=num()
        add=a+5
        return add
    return inner 

@decore1
@decore 
def num():
    return 10
#result=decore(decore1(num))
print(num())