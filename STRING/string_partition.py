#Search for the word "bananas", and return a tuple with three elements:
#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
#anoth
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)