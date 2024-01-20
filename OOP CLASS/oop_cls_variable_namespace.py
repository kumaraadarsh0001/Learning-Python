#Class Variable Namespace
class Mobile:
    fp='Yes'              #class variable
    @classmethod          #class method
    def is_fp(cls):
        print("Finger Print",cls.fp)  #Accessing class variable
realme=Mobile()
redmi=Mobile()
oppo=Mobile()
print("Before modification :")
print("CLASS FP :",Mobile.fp)
print("REALME :",realme.fp)
print("REDMI :",redmi.fp)
print("OPPO :",oppo.fp)
print("\nAfter modification by using class name :")
Mobile.fp="No"    #if you modify by using class name it will change value for all 
print("CLASS FP :",Mobile.fp)
print("REALME :",realme.fp)
print("REDMI :",redmi.fp)
print("OPPO :",oppo.fp)
print("\nAfter modification by using object name :")
realme.fp="Yes fingerprint avilable"  #if you modify by using object it will change only for this object
print("CLASS FP :",Mobile.fp)
print("REALME :",realme.fp)
print("REDMI :",redmi.fp)
print("OPPO :",oppo.fp)