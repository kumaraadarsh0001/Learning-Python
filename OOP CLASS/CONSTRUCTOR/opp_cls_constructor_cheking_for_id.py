#checking for object id 
#constructor with parameter
class Mobile:
    def __init__(self,m): # their __init__ is a constroctor with parameter(m)#here m is a formal argument
        self.model=m
    def show_model(self,p):
        price=p   #local variable
        print(f"Model:{self.model}    Price:{price}")
realme=Mobile("RealMe X7 Pro") #it will give mobile name to parameter(m) #here m is a actual argument
realme.show_model(25000)  #it will give price to parameter(p)
print(id(realme))
print()
redmi=Mobile("Redmi 10 S")
redmi.show_model(12000)
print(id(redmi))
print()
redmi=Mobile("Redmi 10 S")  #in case you can give same name it will create another id for another same name
redmi.show_model(12000)
print(id(redmi))