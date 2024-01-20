#IT GIVES PATH OF YOUR WORKING FILE AND FOLDER NAME
import os
n=os.getcwd()
a=os.walk("d:/important/python")
for i in a:
    print(i)