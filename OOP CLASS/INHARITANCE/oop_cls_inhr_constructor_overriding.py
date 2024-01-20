#Constructor in Inheritance
class Father:        #Fahter class
    def __init__(self,m):  #instant variable 
        self.money=m
        print("Father Class Constructor")
    def show(self):     #Instant Method
        print("Father Class Instance Method")
class Son(Father):     #Son class
    def __init__(self,r):
        self.money=r
        self.car="BMW"
        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance Method",self.money+5000)  #you can also increse money in child class

#If he didn't have constructor, he would take it from his father.
s=Son(3000) #the value of parameter is given to son because it will not call to father's constructor
print(s.money)
print(s.car)
s.disp()
s.show() #Father constructor will not taken but you can call father class instance method