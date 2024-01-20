class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.laptop_name=brand+" "+model
    
    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price-off_price

laptop1=Laptop("hp","au114tx",63000)
laptop2=Laptop("apple","macbook pro",230000)
print(laptop2.apply_discount(20))