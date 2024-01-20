#class encapsulation
class Student:
    __name="Aadarsh"      #__name==private variable
    def __init__(self):
        print(self.__name)   #you can use/accesss private variable in the class
        self.__displayinfo() #you can use/accesss private variable in the class
    def __displayinfo(self):  #__displayinfo==Private Method
        print("Welcome to Python")
obj=Student()
#But you can not use private variable outside of the class 
"print(obj.__name())"        #you can not access with private variable name
"print(obj.__displayinfo())" #you can not access with private variable name