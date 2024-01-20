#Nested clas
class Army:                 #outer class
    def __init__(self):
        self.name="Rahul Yadav"
        self.gn=self.Gun()       #Creating Inner class object
    def show(self):
        print("Name : ",self.name)
    class Gun:
        def __init__(self):
            self.name="AK47"
            self.capacity="75 in one round"
            self.length="34.3 In"
        def disp(self):
            print("Gun Name : ",self.name)
            print("Capacity : ",self.capacity)
            print("Length : ",self.length)
a=Army()
print(a.name)
a.show()
#you can not access sympaly gn.name it will give an error because gn is inner class 
#so you can call outer and then inner class exapmple(a.gn.name=(a is outer class object(gn is inner class object)))
print(a.gn)
print(a.gn.name)
print(a.gn.capacity)
print(a.gn.length)
#another accessing idea for innner class
print()
a.gn.disp()