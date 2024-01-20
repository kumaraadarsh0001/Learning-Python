file=open('student.txt',mode='r')
data=file.readlines()
print(data) #it can return a list of data
for line in data:
    print(line,end='') #their is end= method is used to remove scape secquence in data
file.close()
print('task completed')