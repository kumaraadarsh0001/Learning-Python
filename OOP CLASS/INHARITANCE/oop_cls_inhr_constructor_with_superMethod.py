# Constructor in Inheritance
class Father:  # Fahter class
    def __init__(self, m):  # instant variable
        self.money = m
        print("Father Class Constructor")

    def show(self):  # Instant Method
        print("Father Class Instance Method")


class Son(Father):  # Son class
    def __init__(self, m, j):
        super().__init__(m)  # it will call father class constructor
        self.job = j
        print("Son Class Constructor")

    def disp(self):
        print("Son Class Instance Method", self.money, self.job)


s = Son(500, "Python Developer")  # it will call child class constructor
s.disp()
