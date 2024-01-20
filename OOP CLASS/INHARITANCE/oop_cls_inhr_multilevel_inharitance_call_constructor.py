#Multilevel Inharitance with calling cunstructor
class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Son(Father):   #Simple Inharitance
    def __init__(self):
        super().__init__()       #Calling Father Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

class GrnadSon(Son):  #Multilevel Inharitance
    def __init__(self):
        super().__init__()       #Calling Son Class Constructor
        print("GrandSon Class Constructor") 
    def showGS(self):
        print("GrandSon Class Method")
    
gs=GrnadSon()
# gs.showF()
# gs.showS()
# gs.showGS()