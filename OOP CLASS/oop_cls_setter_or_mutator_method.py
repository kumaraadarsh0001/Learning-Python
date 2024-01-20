#1.setter withoout parameter
class Mobile:
    def __init__(self):
        self.model="realme X"     #Instance variable
    def set_model(self):          #accesser/getter method
        self.model="Redmi Note 10"

realme=Mobile()
#before setting/muting 
print(realme.model)
#After setting/muting
realme.set_model()
print(realme.model)

#2.setter withoout parameter
class Mobile:
    """def __init__(self):
          self.model="realme X"""  #you can not need to write  this two line in accesser with parameter
    def set_model(self,m):  #accesser/getter method
        self.model=m

realme=Mobile()
realme.set_model("oppo reno 8")
print(realme.model)