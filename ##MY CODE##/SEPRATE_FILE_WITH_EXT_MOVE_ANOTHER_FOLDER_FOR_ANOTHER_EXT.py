import os
import shutil
source="D:\\student\\"
dest1="D:\\test\\python files\\"
dest2="D:\\test\\video files\\"
dest3="D:\\test\\picture files\\"
dest4="D:\\test\\pdf files\\"
files=os.listdir(source)
for i in files:
    if i.endswith(".py"):
        shutil.move(source+i,dest1+i)
    if i.endswith(".mp4"):
        shutil.move(source+i,dest2+i)
    if i.endswith(".png"):
        shutil.move(source+i,dest3+i)
    if i.endswith(".pdf"):
        shutil.move(source+i,dest4+i)
print("complete successfily")