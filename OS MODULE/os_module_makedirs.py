#IT CREATE FOLDER(that) IN A FOLDER(this) BOTH
import os 
os.makedirs('this/that') 


import os 
path="c:/KUMAR/AADARSH"             #IT CREATE FOLDER(KUMAR) IN A FOLDER(AADARSH) BOTH
os.makedirs(path)
if not os.path.exists(path):
    os.makedirs(path)
else:
    print('folder is already exists')