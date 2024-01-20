def func(x):
    lst=[]
    n=int(input("enter the size of the list "))
    j=0
    while j<n:
        c=int(input("enter the elements"))
        if(x>c):
            lst.append(c)
        j+=1    
    print(lst)
func(100)
    