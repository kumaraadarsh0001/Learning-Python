from abc import ABC,abstractmethod
#Now here you don't have to write objects, you have to write (ABC).
class Father(ABC):
    #abstract decorator before creating abstract method
    @abstractmethod
    def disp(self):
        #There father cannot write the definition of the class, child class will write the defination.
        pass
    #If you want you can also write a normal method
    def show(self):
        print('Concrete Method')
#we can not create object for father class in abstract method
class Child(Father):
    #write same as father class method
    def disp(self):
        #It is the responsibility of the child to write the definition of the abstract method of the father.
        print("Child Class")
        print("Defining Abstract Method")

c=Child()
c.disp()
c.show()