#create difrent folder for diffrent file extention 
import os
import shutil
source="D:\\##STUDY\\"
files=os.listdir(source)
dest1=os.makedirs("D:\\TEST\\python folder\\")
dest2=os.makedirs("D:\\TEST\\video folder\\")
dest3=os.makedirs("D:\\TEST\\picture folder\\")
dest4=os.makedirs("D:\\TEST\\pdf folder\\")
print("folder is created successfuly")
#copy different extention files in diifrent folders
import os
import shutil
source="D:\\school\\"
dest1="D:\\TEST\\python folder\\"
dest2="D:\\TEST\\video folder\\"
dest3="D:\\TEST\\picture folder\\"
dest4="D:\\TEST\\pdf folder\\"
files=os.listdir(source)
for i in files:
    if i.endswith(".py"):
        shutil.copy(source+i,dest1+i)
    if i.endswith(".mp4"):
        shutil.copy(source+i,dest2+i)
    if i.endswith(".png"):
        shutil.copy(source+i,dest3+i)
    if i.endswith(".pdf"):
        shutil.copy(source+i,dest4+i)
print("complete successfily")