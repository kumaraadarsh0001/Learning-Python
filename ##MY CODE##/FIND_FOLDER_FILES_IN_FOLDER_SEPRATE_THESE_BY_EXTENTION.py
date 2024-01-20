import os
a=[]
b=[]
c=[]
d=[]
x=input('enter path name      =')
y=input('enter folder name    =')
for root, dirs, files in os.walk(f"{x}:/{y}"):
     for name in files:
        print(os.path.join(root, name))
        if name.endswith(".py"):
            a.append(name)
        if name.endswith(".png"):
            b.append(name)
        if name.endswith(".mkv"):
             c.append(name)
        if name.endswith(".pdf"):
             d.append(name)
print("\n####PYTHON FILES####\n",a)
print("\n####PICTURES####\n",b)
print("\n####VIDEOS####\n",c)
print("\n####PDF FILES####\n",d)