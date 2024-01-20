import csv
f=open('csv_fh_write2.csv',mode='w',newline='')  
s_writer=csv.writer(f)
s_writer.writerow(['name','roll_no','marks'])
rec=[]
while True:
    print("Enter student's record:")
    roll_no=int(input('Enter Roll_no:'))
    name=input('Enter name:')
    marks=int(input('Enter marks:'))
    lst=[name,roll_no,marks]
    rec.append(lst)
    ch=input('do you want to enter more records?(y/n)').lower()
    if ch=='n':
        break
s_writer.writerows(rec)
f.close()
print('rest of the code.')