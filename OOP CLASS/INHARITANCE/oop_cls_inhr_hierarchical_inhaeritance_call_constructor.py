#Hierarchical Inharitance
class Father:
    def __init__(self) -> None:
        print("Father Class Constuctor")
    def showF(self):
        print("Father Class Method")

class Son(Father):      #Simple Inharitance
    def __init__(self):
        super().__init__()       #Calling Father Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

class Daughter(Father):  #Simple Inharitance 
    def __init__(self):
        super().__init__()       #Calling Father Class Constructor
        print("Daughter Class Constructor")
    def showD(self):
        print("Daughter Class Method")

s=Son() #Son can use only Father Class method not Daughter Class method 
s.showF()
s.showS()
print()
d=Daughter() #Daugther can use only Father Class Method not Son Class Method
d.showF()
d.showD()