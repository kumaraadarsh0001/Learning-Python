#Accessing Instance Variable Outside class and inside
class Mobile:
    def __init__(self):
        self.model="redmi 10" #Instance Variable
    def show_model(self):   #Instance Method
        self.model    #Accessing Instance Variable
redmi=Mobile()
print(redmi.model) #Accessing Instance Variable outside for class
