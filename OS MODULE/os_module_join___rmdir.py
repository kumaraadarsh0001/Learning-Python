# Python program to explain os.rmdir() method	
# importing os module
import os	
# Directory name
directory = "geeksforgeeks"	
# Parent Directory
parent = "D:/pycharm/"
# Path
path = os.path.join(parent, directory)
# Remove the Directory
# "Geeks"
os.rmdir(path)