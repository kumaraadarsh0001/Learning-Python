#global keywords 
a=10
def func():
    global a
    a=a+20
    print("A =",a)

func()
print("A =",a)


#global keywords from while loop
a=0
def fun():
    global a
    while a<10:
        a+=1
        print(a)
        

fun()
print("global value=",a)