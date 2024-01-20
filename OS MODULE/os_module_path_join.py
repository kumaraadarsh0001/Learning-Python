import os
folder=os.getcwd()
new=os.path.jion(folder,"new folder")
name=os.path.join(new,"sample.txt")
with open(name,"w")as f:
    f.write("some random txt")
