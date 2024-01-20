i=0
def show():
    global i
    i=i+1
    print("love you india",i)
    show()   
show()

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())