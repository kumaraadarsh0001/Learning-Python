for row in range(5):
    for col in range(3):
        if(row*col==0)or(row+col==3)or(row*col==row+col)or(row*col==6)or(row*col==8):
            print("*",end=" ")
        else:
            print("  ",end="")
    print()
