import csv
def read():
    f=open('csv_fh_write1.csv',mode='r',newline='') #if you wnat to read without blank line so we give newline=''.
    s_reader=csv.reader(f)
    for i in s_reader:
        print(i)
read()