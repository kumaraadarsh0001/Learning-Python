#IT GIVES PATH OF YOUR WORKING FILE AND FOLDER NAME
import os 
file=os.walk(r"d:/python")
for current_path,folder,file_name in file:
    #print(f"current path:{current_path}")     #it give current path of all folder 
    print(f"folder location:{folder}")        #it gives all folder in runing folder(python)
    print(f"file name:{file_name}")           #it gives all file from d drive with extention
#
import os
print("current working directory       =",os.getcwd())
os.chdir("C:\\Users\\HP\\OneDrive\\Desktop\\")
print('after change diretory           =',os.getcwd())