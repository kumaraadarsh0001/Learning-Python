file=open('myfile3.txt','w')
#At first it will clear the file and the write the given argument 
#So we can lost our old data in file 
writ=file.writelines(["My name is aadarsh\n","I am a good boy.\n","I want to become a developer"])
#\n given in the last of the second line caractor
#if yoou want to print this line in next so give \n in previous line
#you can given more line but it can write only one line of your given string
file.close
print('task completed')