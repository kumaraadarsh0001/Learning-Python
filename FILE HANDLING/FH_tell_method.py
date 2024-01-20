file=open('myfile3.txt')
print(file.tell())
#initialy the position of cursure is point to zero 
file.read(10)
#after rading caractor the cursur will change their position to given last position of red method
print('AFTER READ 10 CARACTORS IN THE TEXT \nCURSUR POSITION IS:')
print(file.tell())
file.read()
print('AFTER READ ALL DATA FROM THE TEXT \nCURSUR POSITION IS END OF THE TEXT:')
print(file.tell())
file.close