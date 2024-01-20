class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name=name
        self.roll=roll
        self.dob=self.DOB(dd,mm,yy)
    def display(self):
        print(f"Name is {self.name} and roll no is {self.roll}")
        self.dob.display()
    class DOB:
        def __init__(self,dd,mm,yy):
            self.date=dd
            self.month=mm
            self.year=yy
        def display(self):
            print(f"Date of birth is :{self.date}/{self.month}/{self.year}")

st1=Student("lovely boy",101,24,3,2004)
st1.display()