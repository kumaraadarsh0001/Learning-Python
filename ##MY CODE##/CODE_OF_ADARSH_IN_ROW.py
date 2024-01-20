#CODE OF A
def ppa1():
    for row in range(7):
        for col in range(4):
            if(row*col==0)or(row*col==3)or(row*col==9)or(row*col==6 and row+1!=7)or(4+col==7)or(row*col==15)or(row*col==18):#or(row+col==5):#or(row+col==3)or(row*col==row+col):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
ppa1()
print()
#CODE OF D
def ppd():
    for row in range(7):
        for col in range(4):
            if(1*col==0)or(row+col==7)or(row+col==1)or(row*col==9)or(row*col==2 and row+1!=3)or(row*col==6 and row+2!=5):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
ppd()
print()
#CODE OF A
def ppa2():
    for row in range(7):
        for col in range(4):
            if(row*col==0)or(row*col==3)or(row*col==9)or(row*col==6 and row+1!=7)or(4+col==7)or(row*col==15)or(row*col==18):#or(row+col==5):#or(row+col==3)or(row*col==row+col):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
ppa2()
print()
#CODE OF R
def ppr():
    for row in range(7):
        for col in range(4):
            if(1*col==0)or(row+col==1)or(row*col==3)or(row+col==2 and row*col!=1)or(row*col==6 and row+col!=7)or(row*col==4 and row+col!=4)or(row*col==18)or(row*col==10):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
ppr()
print()
#CODE OF S
def pps():
    for row in range(7):
        for col in range(4):
            if(row+col==1)or(row+col==2 and row*col!=1)or(row*col==3)or(row*col==6 and col+2!=5)or(row*col==12)or(row*col==15)or(row+0==5 and 5*col!=5 and 5*col!=10):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
pps()
print()
#CODE OF H
def pph():
    for row in range(7):
        for col in range(4):
            if(1*col==0)or(row*col==15)or(row*col==18)or(0+col==3)or(row*col==9)or(row*col==3)or(row*col==6 and row+col!=7)or(row*col==12 and row+col!=8):
                print("*",end=" ")
            else:
                print("  ",end="")
        print()
pph()