#create difrent folder for diffrent file extention 
import os
import shutil
folder_path=input("enter your folder path=")
source=f"{folder_path}\\"
files=os.listdir(source)
dest1=os.makedirs(f"{folder_path}\\python folder\\")
dest2=os.makedirs(f"{folder_path}\\video folder\\")
dest3=os.makedirs(f"{folder_path}\\picture folder\\")
dest4=os.makedirs(f"{folder_path}\\pdf folder\\")
print("folder is created successfuly")
#copy different extention files in diifrent folders
import os
import shutil
source=f"{folder_path}\\"
dest1=f"{folder_path}\\python folder\\"
dest2=f"{folder_path}\\video folder\\"
dest3=f"{folder_path}\\picture folder\\"
dest4=f"{folder_path}\\pdf folder\\"
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
print("copy items complete successfily")
#example==c:/users/hp/onedrive/desktop/student