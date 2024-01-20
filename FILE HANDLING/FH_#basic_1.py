#writing syntex of file handling as following as:
#file=open("filename",mode='r',"buffering" ,encoding=None,errors=None,newline=None,closefd=True,opener=None)
#encoding= name of the encoding used to decode or encode the file. It should be used only in text mode. Ex:(utf-8)
#closefd= it is use d when you give file scripter as file name
#important :
#filename    mode    buffering    encoding    newline
#mode:
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
#binary mode is sae as noramal mode but:
#'rb'=open for reading. If file doesn't exist it will show "FileNotFoundError" 
#'wb'=open for writing. If any data is already present in the file, it will overwrite the data. If the file dosn't exists it will create that file autometically.
#'xb'=open for exclusive creation with write.it will create a new file and write their.if file is already exitsts it will show error.
#'ab'=open for appending. If file does not  exists it will create a new file for writing data.
#'rb+'=open for reading and writing
#'wb+'=open for writing and then reading. It will overwrite existing data
#'ab+'=open for appending then reading. It won't overwrite existing data