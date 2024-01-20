import os 
current_folder=os.getcwd()
file_name=os.path.join(current_folder, "practice.py")
print(os.path.splitext(file_name))