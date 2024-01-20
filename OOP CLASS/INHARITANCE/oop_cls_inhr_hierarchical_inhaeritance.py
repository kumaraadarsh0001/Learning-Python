# Hierarchical Inharitance
class Father:
    def showF(self):
        print("Father Class Method")


class Son(Father):  # Simple Inharitance
    def showS(self):
        print("Son Class Method")


class Daughter(Father):  # Simple Inharitance
    def showD(self):
        print("Daughter Class Method")


s = Son()  # Son can use only Father Class method not Daughter Class method
s.showF()
s.showS()
d = Daughter()  # Daugther can use only Father Class Method not Son Class Method
d.showF()
d.showD()
