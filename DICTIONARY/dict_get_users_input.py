#getting user input in dictionary
a={}
n=int(input('number of element:'))
for i in range(n):
    key=input('enter your key=')
    value=input('enter your value=')
    a.update({key:value})
print(a)
for j in a:
    print(j)