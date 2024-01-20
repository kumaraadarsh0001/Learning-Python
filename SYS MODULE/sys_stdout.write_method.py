#Standered out is used to output a statement
import sys
print(sys.stdout.write('hellow friends , '))
print(sys.stdout.write('welcome to python world '))
#another example 
import sys
file=open('myfile.txt')
line1=file.readline()
line2=file.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
file.close