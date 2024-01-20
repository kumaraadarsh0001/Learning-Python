#Method overriding
class Add:
    def result(self,a,b):
        print("Addition :",a+b)

class Multi(Add):
    #Super method is used to call parent class's constructor or methods from the child class
    def result(self,a,b):
        super().result(20,20) #here value passed for father(Add) class
        print("Multiply :",a*b)

m=Multi()
m.result(10,20)