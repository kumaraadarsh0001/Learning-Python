#Multiple Inharitance
class Father:
    def showF(self):
        print("Father Class Method")
    
class Mother:
    def showM(self):
        print("Mother Class Method")

class Son(Father,Mother):
    def showS(self):
        print("Son Class Method")

s=Son()
s.showF()
s.showM()
s.showS()