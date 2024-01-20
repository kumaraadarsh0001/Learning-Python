from abc import ABC, abstractmethod

class DeffenceForce(ABC):
    @abstractmethod
    def area(self):
        pass        #for interface
    def gun(self):
        print("Gun  = AK-47") #for abstract
#d=DeffenceForce()   we can not create abject for parent class
class Army(DeffenceForce):
    def area(self):
        print("Area = Land")

class AirForce(DeffenceForce):
    def area(self):
        print("Area = Sky")

class Navy(DeffenceForce):
    def area(self):
        print("Area = Sea")

a=Army()
print("1.For Army :")
a.gun()
a.area()
af=AirForce()
print("\n2.For AirForce :")
af.gun()
af.area()
n=Navy()
print("\n3.For Navy :")
n.gun()
n.area()