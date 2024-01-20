print('#string function old to new string')
name="kumarrraadarsh"
old="kumarrr"
new="kumar"
print(name)
print(name.replace(old,new))


print("#string function split")
name1="hello-how-are-you-baby"
name2="hello how are you baby"
str1=name1.split("-")
str2=name2.split(" ")
print(name1)
print(str1)
print(name2)
print(str2)


print("#string function jiont")
str1=('hello','how','are','you')
a="_".join(str1)
b=" ".join(str1)
print(str1)
print(a)
print(b)