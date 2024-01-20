#
file=open('study3.txt',mode='a+')
print(file.tell()) #pointer position before write mode
file.write('\nlovely \nboy \nbadshah')
print(file.tell()) #pointer position after write mode
file.seek(0)
data=file.read() #it will can't read because pointer position is end of line
print(file.tell()) #pointerposition afer writeing data in file
print(data) 