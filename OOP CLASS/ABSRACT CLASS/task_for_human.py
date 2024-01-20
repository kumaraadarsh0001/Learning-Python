from abc import ABC,abstractmethod
class Human(ABC):
    @abstractmethod
    def  detail(self):
        pass
    def match(self):
        print("human have a name")
        print("human have an age")
        print("human have tow leggs and tow arms")
        
class Human1(Human):
    def detail(self):
        self.name="Aadarsh"
        self.course="Backend"
        self.subject="Python"
        print(f"I am {self.name} learning {self.subject} in {self.course}")
a=Human1()
a.match()
a.detail()
print()
class Human2(Human):
    def detail(self):
        self.name="Dheraj"
        self.course="Backend"
        self.subject="Python"
        print(f"I am {self.name} learning {self.subject} in {self.course}")
a=Human2()
a.match()
a.detail()