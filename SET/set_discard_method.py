a={'Lovely', 10, 12.12, 4560, 'Boy', 'python', 985}
print('before discarding',id(a))
x='python'
y='aadarsh'
a.discard(x)
a.discard(y)  #it will not give any error whether element is there or not
print(a)
print('after discarding',id(a))
