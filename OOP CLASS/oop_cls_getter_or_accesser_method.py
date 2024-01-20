class Mobile:
    def __init__(self):
        self.model="realme X"     #Instance variable
    def get_model(self):          #accesser/getter method
        return self.model

realme=Mobile()
m=realme.get_model()
print(m)