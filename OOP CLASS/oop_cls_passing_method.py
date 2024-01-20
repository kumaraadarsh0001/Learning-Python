#Raking input from user 
a=input('Enter your name:')
b=input('Enter your roll:')
#Passing member of one class to another class
class Student:
    #Constructor
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    #Instance method
    def disp(self):
        print("Student Name : ",self.name)
        print("Student Roll : ",self.roll)
class User:
    #Static Method
    @staticmethod
    def show(s):
        print("User Name : ",s.name)
        print("User Roll : ",s.roll)
        s.disp()   #it will call disp method from student class

#Creating obect of student class
stu=Student(a,b)

User.show(stu)