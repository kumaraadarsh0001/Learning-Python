"""create a class form user input a integer number
    you will give roman number of this integer
    and then you will reverse into roman number"""
class Roman:
    def int_to_rom(self):
        x=int(input("Eenter your integer number :"))
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
        i = 12  
        roman_numeral = ''
        while x != 0:
            if numbers[i] <= x:    
                roman_numeral += roman[i] 
                x = x - numbers[i]
            else:
                i -= 1 # i = i - 1
        print(roman_numeral)

    def rom_to_int(self):
        pass

def call():
    print("""        Press 1 for convert integer to roman
        Press 2 for convert roman to integer""")
    ch=int(input("Enter for choice 1 or 2 :"))
    if ch==1:
        r=Roman()
        r.int_to_rom()
    elif ch==2:
        print("some other ")
    else:
        print("Please chose a correct option")
        call()
call()