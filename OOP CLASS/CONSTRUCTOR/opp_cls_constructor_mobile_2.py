class Mobile:
    #constructor with parameter 
    def __init__(self,m):
        self.model=m
    def show_model(self,p):
        self.price=p 
        print("Model:",self.model,"\nPrice:",self.price)

realme=Mobile("RealMe X7 Pro") #it will give mobile name to parameter(m)
realme.show_model(25000)  #it will give price to parameter(p)
