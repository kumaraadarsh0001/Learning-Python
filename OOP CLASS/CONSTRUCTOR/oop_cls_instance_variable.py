class Student:
    pass
anish=Student()
#creating instance variable for anish
anish.name="Anish"
anish.std="12th"
anish.sec="B"
anish.sub=['ENGLISH','HINDI','MATH','PHYSICS','CHEMISTRY']
aadarsh=Student()
#creating instance variable for aadarsh
aadarsh.name="Aadarsh"
aadarsh.std="12th"
aadarsh.sec="B"
aadarsh.sub=['ENGLISH','HINDI','MATH','PHYSICS','CHEMISTRY']
#it will give a genrator object
print(anish,aadarsh)
#printing instance variable of anish and aadarsh 
print(f"Name:{anish.name}\nClass:{anish.std}\nSection:{anish.sec}\nSubjects:{anish.sub}")
print(f"Name:{aadarsh.name}\nClass:{aadarsh.std}\nSection:{aadarsh.sec}\nSubjects:{aadarsh.sub}")