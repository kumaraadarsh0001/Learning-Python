file_name=input('enter your file name:')
file=open(file_name,mode='r')
number_of_words=0
number_of_charactors=0
number_of_lines=0
for line in file:
    number_of_lines+=1
    line=line.strip('\n')
    number_of_charactors+=len(line)
    list1=line.split()
    number_of_words+=len(list1)
file.close
print('number_of_lines=',number_of_lines)
print('number_of_words=',number_of_words)
print('number_of_charactors=',number_of_charactors)