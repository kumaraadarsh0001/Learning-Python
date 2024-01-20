#Multilevel Inharitance
class Father:
    def showF(self):
        print("Father Class Method")

class Son(Father):   #Simple Inharitance
    def showS(self):
        print("Son Class Method")

class GrnadSon(Son):  #Multilevel Inharitance 
    def showGS(self):
        print("GrandSon Class Method")
    
gs=GrnadSon()
gs.showF()
gs.showS()
gs.showGS()