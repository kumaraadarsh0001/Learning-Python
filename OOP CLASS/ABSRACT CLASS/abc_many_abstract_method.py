from abc import ABC,abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def disp(self):
        pass
class Child(Parent):
#if you have 2 abstract methods and you can define for one it can't run and give an error
    def show(self):
        print("Child class")
        print("Disp 1 abstract method")
#So define all abstract method in child class 
"""so you can not crate object for chuld class
c=Child
c.show()"""
class GrandChild(Child):
    def disp(self):
        print("GrandChild class")
        print("Disp 2 abstract method")
#here you can call grand child because all method of parent will define 
gd=GrandChild()
gd.show()
gd.disp()