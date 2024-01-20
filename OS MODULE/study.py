from genericpath import exists
import os
import sys
import shutil
folder_path=input('enter folder path:')
#check if folder exists
if exists(folder_path):
    print('folder is exists')
else:
    print('folder path not exists')
    sys.exit()
#check if folder is empty
if os.listdir(folder_path):
    print('folder is not empty')
else:
    print('folder is empty')
    sys.exit()
#check for files
audio_files=['.mp3','.wav','wma','.aac','flac','.ogg','.m4a','.aiff','.alac']
image_files=['.jpg','.jpeg','.png','.gif','.tiff','.psd','raw','.bmp','heif','.indd','.svg','.ai','.eps']


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
    if i.endswith(image_files):
        shutil.copy(source+i,dest1+i)
    if i.endswith(".mp4"):
        shutil.copy(source+i,dest2+i)
    if i.endswith(".png"):
        shutil.copy(source+i,dest3+i)
    if i.endswith(".pdf"):
        shutil.copy(source+i,dest4+i)
print("copy items complete successfily")