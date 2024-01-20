file=open('myfile1.txt')
#it will print step of 2 line because there was also present new line in the document
print(file.readline())  #it will read first line in the text document
print(file.readline())  #it will read second line in the text document
print(file.readline())  #it will read third line in the text document
print(file.readline())  #it will read fourth line in the text document
print(file.readline())  #it will read only that line was exist so 5th readline function can't work
file.close
#another
file=open('myfile2.txt')
all_line=file.readlines() #it will print all line in a list one by one 
print(all_line)
file.close