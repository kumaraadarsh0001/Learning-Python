file=open('C:/Users/HP/OneDrive/Desktop/autocreate.txt' , 'w')
#At first it will clear the file and the write the given argument 
#So we can lost our old data in file 
file.write('Hey how are you. ')
file.write('\nI am your best friend.')  #\n given next line caractor
file.write('\nI want to meat you.')  #if yoou want to print this line in next so give \n in previous line
#you can given more line but it can write only one line of your given string
file.close
print('well done task completed')