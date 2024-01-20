# if elif else statement
day=input('enter the day today')
if (day=='monday'):
    print("today is monday")
elif (day=='tuesday'):
    print("today is tuesday")
elif (day=='wednesday'):
    print("today is wednesday")
else:
    print("holiday")
# if elif else statement
a=input('enter your name')
b=int(input('enter your english test number'))
c=int(input('enter your hindi test number'))
d=int(input('enter your maths test number'))
sum=b+c+d
sum=(sum/3)
if sum>=90:
    print("Excelant beta")
elif sum>=70:
    print("Very good student")
elif sum>50:
    print("Good student")
else:
    print('poor boy')