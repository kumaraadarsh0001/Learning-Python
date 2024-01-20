import os
#if you want to create and write something in a file 
#it is atomaticaly create a file given by you
file = os.popen("Hello.txt", 'w')
file.write("Hello there! This is a tutorialspoint article")