a=1
b=5
print("##if you play the game")
print("##enter the number between 1to10")
print("##you have only 5 chanches")
while a<=b:
    c=int(input("enter your number="))
    if c==7:
        print("you are winner")
        break
    elif c==6:
        print("closer form number")
    elif c==8:
        print("closer form number")
    else:
        print("better luck play again")
    a+=1
if c<=5:
    print("##GAME OVER##")