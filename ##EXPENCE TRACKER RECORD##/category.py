import os
import csv
import datetime
if os.path.exists('category.csv'):
    file=open("category.csv","a",newline="")
    s_writer=csv.writer(file)
else:
    file=open("category.csv","w",newline="")
    s_writer=csv.writer(file)
    s_writer.writerow(['CATEGEORY','DATE_TIME'])
cat_rec=[]
while True:
    categery=input('Enter your categery name :')
    date_time=datetime.datetime.now()
    lst=[categery,date_time]
    cat_rec.append(lst)
    ch=input('do you want to enter more records?(y/n)').lower()
    if ch!='y':
        break
for i in cat_rec:
    s_writer.writerow(i)
file.close()
print('categery opretion completed')