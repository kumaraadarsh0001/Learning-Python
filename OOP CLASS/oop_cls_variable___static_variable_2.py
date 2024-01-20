#Class/Static variable with class Method
class Mobile:
    fp='Yes'                        #Class variable

    def __init__(self):             #Instance variable
        self.model='realme X'

    def show_model(self):           #Instance method      
        print("Model:",self.model)  #Acccessing Instance Variable

    @classmethod                    #Class Method
    def is_fp(cls):
        print("Finger Print",cls.fp)#Accessing Class Variable inside from class method
print("Before modificaton :")
realme=Mobile()
realme.show_model()     #calling instant method 
Mobile.is_fp()          #calling class method
print()
print("After mpdification :")
Mobile.fp="No"          #modifying vale of fp in to class variable
Mobile.is_fp()          #calling class method