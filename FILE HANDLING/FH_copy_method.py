#it will recive data from given file
file1=open('study3.txt', mode='r')
#it will write data into given file
file2=open('ACFTCE.txt', mode='w')
data=file1.read()
file2.write(data)
file1.close()
file2.close()
print('task completed successfully.')