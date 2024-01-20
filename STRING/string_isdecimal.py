#Check if all the characters in the unicode object are decimals
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
