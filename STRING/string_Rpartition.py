#Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)