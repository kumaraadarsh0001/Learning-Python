import os 
path="d:/python/os module/practice.py"
fd=os.open(path,os.O_RDONLY)
status=os.fstat(fd)
print(status)
os.close(fd)