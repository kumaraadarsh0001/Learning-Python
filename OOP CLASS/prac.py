def int_to_rome():
    x=input("enter your number :")
    roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    for i in roman:
        if i=="I" :
            print(1)
int_to_rome()
# print(int_to_rome(4))
# print(int_to_rome(1249)) 
# print(int_to_rome(67))
