#it can read file first and then write in the file
file=open('study1.txt',mode='r+')
print(file.tell()) #pointer position before read mode
data=file.read()
file.write('\nhey how are you')
print(file.tell()) #pointer position after read mode
print(data)
print(file.tell()) #pointerposition afer writeing data in file