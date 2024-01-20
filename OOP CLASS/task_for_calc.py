print("FOR CALCULATOR OPRATION")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
class Calculator:
    def add(self):      #Method for addition
        print(a+b)
    def sub(self):      #Method for substration
        print(a-b)
    def multiply(self): #Method for addition
        print(a*b)
    def divide(self):   #Method for addition
        print(a/b)
    def squre(self):    #Method for square
        print(a**b)
    def modulus(self):  #Method for modulus
        print(a%b)
obj=Calculator()
def calc():
    print("1.ADDITON      2.SUBSTRACTION      3.MULTIPLY      4.DIVISION      5.SQUARE      6.MODULUS")
    ch=int(input("Enter your choice:"))
    if ch==1:
        obj.add()
    elif ch==2:
        obj.sub()
    elif ch==3:
        obj.multiply()
    elif ch==4:
        obj.divide()
    elif ch==5:
        obj.squre()
    elif ch==6:
        obj.modulus()
    else:
        print("please enter from given number")
        calc()
calc()