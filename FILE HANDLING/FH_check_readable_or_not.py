#chek file is readable or not 
file=open('myfile1.txt','r')
print('file is readable =',file.readable())
print('file is writable =',file.writable())
file.close
#check file is writeable or not
file=open('myfile1.txt','w')
print('file is writable =',file.writable())
print('file is readable =',file.readable())
file.close