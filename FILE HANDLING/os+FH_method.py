import os
file_name=input('enter your file name=')
if os.path.isfile(file_name):
    file=open(file_name)
    print('file opened successfully.')
    data=file.readlines()
    for line in data:
        print(line,end='')
    file.close
    print('\nfile closed successfully.')
else:
    print('file not found')