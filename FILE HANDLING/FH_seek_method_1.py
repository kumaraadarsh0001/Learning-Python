#remember, file pointer position is always counted from the begining(0).
file=open('myfile3.txt')
print(file.tell())
print(file.read(25))
#Seek method is used to change the cursur position
#you can give any starting point to seek method
file.seek(18) #it will start from the given argument 
print(file.read())
file.close