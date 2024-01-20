
str1="kumar aadarsh"
str2='kumar aadarsh'
str3='''helow world'''
str4=str3
print("str1=",id(str1))
print("str2=",id(str2))
print("str3=",id(str3))
print("str4=",id(str4))

#when value is change then id is changed
str1= "lovely boy"
print("str1=",id(str1))
str2= "aadarsh kumar"
print("str2=",id(str1))
