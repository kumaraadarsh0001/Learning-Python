a={'Lovely', 10, 12.12, 4560, 'Boy', 'python', 985}
print('before cliaring',a)
print(id(a))
a.clear()
print("after clearing",a)
print(id(a))