#Accessing Instance Variable
class Mobile:
    def __init__(self):
        self.model="redmi 10" #Instance Variable
    def show_model(self):   #Instance Method
        self.model    #Accessing Instance Variable
redmi=Mobile()
realme=Mobile()
oppo=Mobile()
#Accessing Instance Variable outside for class
print("Before modification :")
print(redmi.model)
print(realme.model)
print(oppo.model)
print("After modification :")
realme.model="RealMe X"
print(redmi.model)
print(realme.model)
print(oppo.model)