file=open('image 2.jpg','rb')

newfile=open('newtxtfile.txt','wb')

for line in file:
    newfile.write(line)

file.close()
newfile.close()