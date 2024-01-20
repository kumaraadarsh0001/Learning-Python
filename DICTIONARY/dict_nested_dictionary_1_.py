#nested dictionary
a={'course':'Python','fees':72990,1:{'course':'Java Script','fees':72990}}
print(a)
print(a['course'])
print(a['fees'])
print(a[1])
print(a[1]['course'])
print(a[1]['fees'])
#modifing nested dictionary
print('after modification dictionary:')
a['course']='machine learning'
a[1]['duration']='6 month'
a[2]={'course':'C++','fees':71999}
print(a)