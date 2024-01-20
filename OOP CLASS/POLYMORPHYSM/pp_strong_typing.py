#hasattr(): Function is used to check wether the object has a method or not
class Duck:
    def walk(self):
        print('Duck walk sound :')
        print("Thapak Thapak Thapak Thapak")

class Horse:
    def walk(self):
        print('Horse walk sound :')
        print("Tabdak Tabdak Tabdak Tabdak")

class Cat:
    def talk(self):
        print('Cat talk sound :')
        print("Meow Meow Meow")

def my_function(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()

d=Duck()
my_function(d)
print()
h=Horse()
my_function(h)
print()
c=Cat()
my_function(c)