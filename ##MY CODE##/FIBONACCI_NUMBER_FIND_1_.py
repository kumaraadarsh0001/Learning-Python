#function to find fibonacci number
def fun(n):
   if n <= 1:
       return n
   else:
       return(fun(n-1) + fun(n-2))
n=int(input("enter your number="))
#for loop in if statement 
if n<=0:
   print("not define for this no.")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fun(i))