class Mobile:
    #constructor
    def __init__(self,m,v=80): #here 80 is default value of variable(v)
        self.model=m
        self.volumn=v
    def show_model(self,p):
        price=p
        print("Model:",self.model,"\nPrice:",price,"\nVolumn:",self.volumn)
#Passing argument to constructor
realme=Mobile("RealMe X",50)  #if 50 is not given then volumn take default value
#Accessing Method from outside Class
realme.show_model(20000)
print()
redmi=Mobile("Redmi Note 10")
redmi.show_model(10000)