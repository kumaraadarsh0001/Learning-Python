#code for expence tracker 
import csv
from datetime import datetime
import os
import random
dt=datetime.today()
for row in range(5):
    for col in range(5):
        if (0+col==0)or(0+col==1 and row+col!=2 and row+col!=4)or(0+col==2 and row*col!=2 and row*col!=6)or(0+col==4 and row*col!=16 and row*col!=8 and row+col!=12 and row+col!=4):
            print("##",end=" ")
        else:
            print("  ",end=" ")
    print()
for row in range(5):
    for col in range(31):
        if (0+col==4 and row*col!=4 and row*col!=8 and row*col!=12 and row*col!=16)or(0+col==5)or(0+col==8)or(0+col==12)or(0+col==14)or(0+col==16)or(0+col==20)or(0+col==24)or(0+col==6 and row*col!=6 and row*col!=12 and row*col!=18 and row*col!=24)or(0+col==9 and row*col!=9 and row*col!=36)or(0+col==10 and row*col!=30)or(row*col==10)or(row*col==18 and row+col!=9 and row+col!=19)or(row*col==20)or(row*col==27 and row+col!=28)or(row*col==40)or(0+col==13 and row*col!=13 and row*col!=39 and row*col!=52)or(row*col==26 and row+col!=27)or(0+col==18 and row*col!=54 and row*col!=36 and row*col!=18)or(0+col==17 and row*col!=17 and row*col!=34 and row*col!=51)or(row*col==68)or(row*col==72)or(0+col==22 and row*col!=66 and row*col!=22 and row*col!=44)or(row*col==21 and row+col!=10)or(row*col==63)or(row*col==88)or(0+col==25 and row*col!=75 and row*col!=25)or(0+col==26 and row*col!=78 and row*col!=26)or(row*col==50)or(row*col==52 and row+col!=17)or(row*col==96)or(row*col==100)or(row*col==104)or(0+col==28)or(row*col==28 and row+col!=11)or(0+col==29 and row*col!=29 and row*col!=116)or(0+col==30 and row*col!=90)or(row*col==30 and row+col!=13 and row+col!=17)or(row*col==56)or(row*col==58)or(row*col==60 and row+col!=19)or(row*col==84 and row+col!=25)or(row*col==87)or(row*col==112)or(row*col==120):
            print("##",end=" ")
        else:
            print("  ",end=" ")
    print()  
print()
def sol():
    print("WELCOME TO EXPENCE TRADCKER!!!")
    print("1.SignUP               2.Login")
    syl=int(input("CHOSE ONE OPTION :"))
    if syl==1:
        if os.path.exists("pw_manager.csv"): #if file alredy exists it will open in append mode 
            file=open("pw_manager.csv",mode='a',newline="")
            s_writer=csv.writer(file) 
        else: #if file not exists it will create a file with heading 
            file=open("pw_manager.csv",mode='a',newline="")
            s_writer=csv.writer(file)
            s_writer.writerow(['#NAME#','#USER_ID#','#GMAIL#','#PASSWORD#'])
        rec=[]
        name=input('enter your name :').upper() #upper will convert name in upper case
        gmail=input("enter your gamil :")
        password=input("enter your password :")
        user=random.randrange(10000,100000) #it will give any number between range
        userid=f"{name}{user}"
        lst=[name,userid,gmail,password]
        rec.append(lst)
        for i in rec:
            s_writer.writerow(i)
        print("1.APPEND MY DATA               2.DON'T APPEND MY DATA")
        ap_ch=int(input("Enter a number from 1/2  :"))
        if ap_ch==1:
            def expence():
                if os.path.exists('expence.csv'):#if file exists it will open file in append mode 
                    expence_file=open("expence.csv","a",newline="")
                    s_writer=csv.writer(expence_file) 
                else:                 #if file dosn't exists it will create a file in write mode
                    expence_file=open("expence.csv","w",newline="")
                    s_writer=csv.writer(expence_file)
                    s_writer.writerow(['USER_ID','EXPENCE','DISCRIPTION','AMOUNT','CATEGEORY','DATE_TIME'])
                rec=[]
                categorys=[{'name':"RENT",'id':1},
                        {'name':"BILL",'id':2},
                        {'name':"GROSERY",'id':3},
                        {'name':"PETROL",'id':4}]
                while True:
                    date_time=dt.strftime("%B,%d,%Y  %H:%M:%S")
                    expence=input('Enter your expence :')
                    discrition=input('Enter your discription :')
                    amount=int(input('Enter your amount :'))
                    print("""select categeory:
                            1.RENT   2.BILL   3.GREOSRY   4.PETROL""")
                    choice=int(input('Enter number from categeory :'))
                    for cate in categorys:
                        if cate["id"]==choice:
                            lst=[userid,expence,discrition,amount,cate['name'],date_time]
                    rec.append(lst)
                    ch=input('do you want to enter more records?(y/n)').lower()
                    if ch!='y':
                        break
                for i in rec:
                    s_writer.writerow(i)
                print('*****YOUR EXPENCE UPDATE SUCCESSFULY..\n     IF YOU WANT TO SEE THIS PLEASE LOGIN THE APP*****')
                expence_file.close()
            expence()
        else:
            print("THANK'S FOR SIGNIN \nIF WANT TO CREATE YOUR EXPENCE VISIT AND LOGIN FROM GAMIL PASSWORD")
    elif syl==2:
        def login():
                gmail=input("enter your gmail :")
                password=input("Enter your password :")
                data_gmail=[]
                data_pswrd=[]
                all_data=[]
                with open('pw_manager.csv') as pw_file:
                    reader=csv.reader(pw_file)
                    for row in reader:
                        all_data.append(row)#it will append all data to a list which name is all_data
                        data_gmail.append(row[2]),data_pswrd.append(row[3])#it will append gmail in data_gmail list and password in data_pswrd list
                data_gmail.remove("#GMAIL#"),data_pswrd.remove("#PASSWORD#")#it will remove heading into csv file(pw_manager)
                for gm in data_gmail:#this loop will execute when gmail and password will correct
                        if gm==gmail:
                            for pw in data_pswrd:
                                if pw==password:
                                    print()
                    # for gm in data_gmail:#this loop will exucute when gmail is not correct
                    #     if gm!=gmail:
                    #         print("\ngmail not found\n")
                    #         login()
                    # for pw in data_pswrd:#this loop will exucute when password is not correct
                    #     if pw!=password:
                    #         print("\npassword is incorrect\n")
                    #         login()
                for list in all_data:
                    if list[2]==gmail:
                        if list[3]==password:
                            print(f"NAME:       {list[0]}")#it will print name which is already in csv file index[0]
                            print(f"USER ID:    {list[1]}")#it will print user_id which is already in csv file index[0]
                            def data_append():
                                print("1.APPEND MY DATA               2.DON'T APPEND MY DATA")
                                syl=int(input("CHOSE ONE OPTION :"))
                                if syl==1:           
                                    def expence():#it will open expence file for append data in this file 
                                        if os.path.exists('expence.csv'):
                                            expence_file=open("expence.csv",mode="a",newline="")
                                            s_writer=csv.writer(expence_file)
                                        else:#it will create a file which name is expence.csv for writing data in this
                                            expence_file=open("expence.csv","w",newline="")
                                            s_writer=csv.writer(expence_file)
                                            s_writer.writerow(['USER_ID','EXPENCE','DISCRIPTION','AMOUNT','CATEGEORY','DATE_TIME'])#this is the heading to write in this file 
                                        rec=[]#this is the list of all data record
                                        categorys=[{'name':"RENT",'id':1},
                                                {'name':"BILL",'id':2},
                                                {'name':"GROSERY",'id':3},
                                                {'name':"PETROL",'id':4}]#this is the category to given for choice by user
                                        while True:
                                            date_time=dt.strftime("%B,%d,%Y  %H:%M:%S") 
                                            expence=input('Enter your expence :')
                                            discrition=input('Enter your discription :')
                                            amount=int(input('Enter your amount :'))
                                            print("""select categeory:
                                                    1.RENT   2.BILL   3.GREOSRY   4.PETROL""")
                                            choice=int(input('Enter number from categeory :'))
                                            for cate in categorys:
                                                if cate["id"]==choice:
                                                    #up_cat.append(cate["name"])
                                                    lst=[list[1],expence,discrition,amount,cate['name'],date_time]
                                            rec.append(lst)
                                            ch=input('do you want to enter more records?(y/n)').lower()
                                            if ch!='y':
                                                break
                                        for i in rec:
                                            s_writer.writerow(i)
                                        print('*****YOUR EXPENCE UPDATE SUCCESSFULY..*****')
                                        expence_file.close()
                                    expence()
                                elif syl==2:
                                    print("\n*****YOU HAVE NOT TO APPEND\n     THANKS FOR USING THIS APP*****")
                                    exit()
                                else:
                                    print('enter for 1 or 2 not another')
                                    data_append()
                                    print()
                            def show_data():
                                print("1.SHOW MY DATA                 2.DON'T SHOW MY DATA")
                                syl=int(input("CHOSE ONE OPTION :"))
                                if syl==1:
                                    with open("expence.csv",mode="r") as file3:
                                        f_reader=csv.reader(file3)
                                        for my_exp in f_reader:
                                            if my_exp[0]==list[1]:
                                                my_exp.remove(list[1])
                                                print("['EXPENCE','DISCRIPTION','AMOUNT','CATEGEORY','DATE_TIME']")
                                                print(my_exp)
                                    data_append()
                                    print()
                                    
                                elif syl==2:
                                    data_append()
                                else:
                                    print('enter for 1 or 2 not another')
                                    show_data()
                            show_data() 
        login()   
sol()
#only a problem it will run after you enter GMAIL in gmail and PASSWORD in password
#cheking for all test for this app is complete 
#this app is complete for using