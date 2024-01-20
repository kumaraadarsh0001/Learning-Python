#Polymorphysm in class 
class Duck:
    def walk(self):
        print("Thapak Thapak Thapak Thapak")

class Horse:
    def walk(self):
        print("Tabdak Tabdak Tabdak Tabdak")

def my_function(obj):
    obj.walk()

d=Duck()
h=Horse()
print('Duck walk sound :')
my_function(d)
print('Horse walk sound :')
my_function(h)