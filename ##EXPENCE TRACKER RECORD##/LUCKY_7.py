import random
def call():
    small=[2,3,4,5,6]
    big=[8,9,10,11,12]
    num=int(input("ENTER YOUR NUMBER :"))
    rang=random.randrange(2,13)
    print(rang)
    if rang in small:
        if num==2 or num==3 or num==4 or num==5 or num==6:
            print("SMALLER NUMBER IS OPEN\nYOU HAVE WINNER")
        else:
            print("SMALLER NUMBER IS OPEN\nBETTER LUCK PLEASE TRY AGAIN")
    elif rang in big:
        if num==8 or num==9 or num==10 or num==11 or num==12:
            print("BIGGER NUMBER IS OPEN\nYOU HAVE WINNER")
        else:
            print("BIGGER NUMBER IS OPEN\nBETTER LUCK PLEASE TRY AGAIN")
    else:
        if num==7:
            print("LUCKY 7 IS WINNER\nYOU HAVE WINNER")
        else:
            print("LUCKY 7 IS WINNER\nBETTER LUCK PLEASE TRY AGAIN")   
def pl():
    play=int(input('PRESS 1 FOR PLAY AND 2 FOR EXIT ='))
    if play==1:
        print("""   YOUR CHOICE SHOULD BE FROM THESE NUMBERS :
                    SMALLER  = [2,3,4,5,6]
                    LUCCKY   = 7
                    BIGGER   = [8,9,10,11,12]    """)
        call()
        pl()
    elif play==2:
        print("THANKS FOR PLAYING")
        exit()
    else:
        print("PLEASE ENTER VALID NUMBER FROM 1 OR 2")
        pl()
pl()