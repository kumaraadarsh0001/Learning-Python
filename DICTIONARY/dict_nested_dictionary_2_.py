#nested dictionary
a={1:{'course':'Python','fees':72990,'duration':'6 month'},
   2:{'course':'Java Script','fees':73990,'duration':'6 month'}}

print(a[1])
print(a[1]['course'])
print(a[1]['fees'])
print(a[1]['duration'])
print()
print(a[2])
print(a[2]['course'])
print(a[2]['fees'])
print(a[2]['duration'])
#modification 
print('after modification dictionary:')
a['course']='machine learning'
a[1]['duration']='6 month'
a[2]={'course':'C++','fees':71999}
print(a)