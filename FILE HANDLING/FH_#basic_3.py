##binary mode doesn't take an encoding argumen
#cheking method for binary reading mode:
f=open("myfile1.txt",mode="rb")
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
print()
#cheking method for binary writing mode:
f=open("myfile1.txt",mode="wb")
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
print()
#cheking mehtod for binary appending:
f=open("myfile1.txt",mode="ab")
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
print()
#cheking method for "x" mode in file handling
f=open("lovly_boy.txt",mode="xb")
#it will create a file the file is exists it will shows error
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
#checking method for readmode:
f=open("myfile1.txt",mode="rb+")
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
print()
#checking method for writemode:
f=open("myfile1.txt",mode="wb+")
print('FILE NAME =',f.name)
print('FILE MODE =',f.mode)
print('FILE IS READABLE =',f.readable())
print('FILE IS WRITEABLE =',f.writable())
print('FILE IS CLOSED =',f.closed)
f.close()
print('FILE IS CLOSED =',f.closed)
print()