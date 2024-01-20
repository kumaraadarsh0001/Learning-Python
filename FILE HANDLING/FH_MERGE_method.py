files=[]  #thier are append all files from users input.
merged_data=''
while True: 
    f_name=input('enter your file name:') #it is used to get file_name(f_name) from users
    files.append(f_name)  #it is used to append all file from given by user to append in a list(files)
    ans=input('Want to add another file?(y/n)').lower() #it is used to ask any other file if yes then (.lower()) is convert in lower case if you enter in any formate
    if ans!='y': #if user enter n so code is exit and another line of code starts run
        break
for file in files:  #it take all file from a list(files)
    filename=file+'.txt'  #it wiil add filename+extention(file+.txt)
    f=open(filename,mode='r',encoding='utf-8')  #it will open file to read
    merged_data=merged_data+f.read()+'\n'  #it is used to merge all data from given files.
    f.close()   #it wiil close all file 
print(files)  #it will print file names in a list
print(merged_data)  #it will print all merged data