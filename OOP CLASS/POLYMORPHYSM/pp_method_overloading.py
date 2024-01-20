#Method overloading in class 
class OL_method:
    #you can not add int type with none type
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(f"Addition of all numbers:{a},{b},{c}")
            x=a+b+c
        elif a!=None and b!=None:
            print(f"Multiplication of given numbers :{a},{b}")
            x=a*b
        elif a!=None:
            print(f"Square of given number :{a}")
            x=a**2
        return x
    
ol=OL_method()
print(ol.sum(10,20,30))
print(ol.sum(10,20))
print(ol.sum(20))