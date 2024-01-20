file=open('myfile1.txt','r') #This r is a default value that will not matter if the code is written or not.
content=file.read(55) #this will print only first 20 caractors
content2=file.read()
print('#FIRST 20 CARACTORS IN FILE:')
print(content)
print()
print('21st to last CARACTORS IN THE FILE:')
print(content2) #this will print anothor caractor except this first 20 caractors
file.close()
