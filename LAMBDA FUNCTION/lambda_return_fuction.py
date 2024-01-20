#lambda return functoion
def show():
    y=21
    return (lambda x:x+y)
    
a=show()
print(a(12))