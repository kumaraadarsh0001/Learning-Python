#Constructor in Inheritance
class Father:        #Fahter class
    def __init__(self,m):  #instant variable 
        self.money=m
        print("Father Class Constructor")
    def show(self):     #Instant Method
        print("Father Class Instance Method")
class Son(Father):     #Son class
    def disp(self):
        print("Son Class Instance Method",self.money+5000)  #you can also increse money in child class
#It is the responsibility of the child to pass the value in parameter
s=Son(5000) #it will call automaticaly to father instant variable
print(s.money) #you can access only instance variable for this type not instant method
s.show() #Father class method inharite
s.disp() #child class own method