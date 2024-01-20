#IT CAN CHECK FOLDER IS EXISTS 
import os 
if not os.path.exists("new folder"):
    os.makedirs("new folder")    #IF FILE IS NOT EXISTS IT CAN CREATE NEW FOLDER
else:
    print('path exists')