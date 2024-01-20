#Accessing class/static varible
class Mobile:
    ka="KUMAR"  #class variable
    @classmethod  #decorator 
    def is_ka(cls):
        print(cls.ka)  #Accessing class variable from inside of class

realme=Mobile()
Mobile.is_ka()  #calling class method
print()
print(Mobile.ka)  #Accessing class variable from outside of class
Mobile.ka="AADARSH"  #modifying value of class varible from outside
Mobile.is_ka()  #calling class method