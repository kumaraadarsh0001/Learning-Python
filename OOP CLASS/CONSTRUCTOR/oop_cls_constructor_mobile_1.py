#Example 2
#constructor without parameter
class Mobile:
    def __init__(self): #__init__ is a constroctor
        self.model="RealMe X"
    def show_model(self):
        price=20000     #local variable 
        print("Model:",self.model,"\nPrice:",price)

realme=Mobile()
realme.show_model()
realme.model="RealMe X7 Pro"   #it will change the model name
realme.show_model()