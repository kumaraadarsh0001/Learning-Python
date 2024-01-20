#Single inharitance 
class Father:
    money=1000
    def show(self):
        print("Parent class instance method")
    @classmethod
    def showmoney(cls):
        print("Parent class class method",cls.money)
    @staticmethod
    def stat():
        a=500
        print("Parent class Static method",a)
    
class Son(Father):
    def disp(self):
        print("Child class instance method")
#You can access son class instance method thier
s=Son()
s.disp()
#you can access father class from son class 
#this method is actualy define in parent clas but access in son class
s.show()
s.showmoney()
s.stat()
print()
#father class access
f=Father()
f.show()
f.showmoney()
f.stat()
#Impprtant
#1.We can access Parent Class Variable and Method using Child Class Object.
#2.We can also access Parent Class Variable an Methods using Parent Class Object.
#3.We can not access Child Class Variable and Method using Parent Class object.