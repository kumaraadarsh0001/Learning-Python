#it can write in file first and then read the file
file=open('study2.txt',mode='w+')
print(file.tell()) #pointer position before write mode
file.write('\nhey how are you')
print(file.tell()) #pointer position after write mode
file.seek(0)
data=file.read() #it will can't read because pointer position is end of line
print(file.tell()) #pointerposition afer writeing data in file
print(data) 