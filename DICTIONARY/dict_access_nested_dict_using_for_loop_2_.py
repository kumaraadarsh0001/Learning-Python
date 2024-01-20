a={1:{'course':'Python','fees':72990,'duration':'6 month'},
   2:{'course':'Java Script','fees':73990,'duration':'6 month'}}
print('ID')
for id in a:
    print(id)
print()
#keys
print('KEYS')
for id in a: 
    for key in a[id]:
        print(key,'=',a[id][key])
print()

#anothoer nested accessing dictionary
"""a={1:{'course':'Python','fees':72990,'duration':'6 month'},
   2:{'course':'Java Script','fees':73990,'duration':'6 month'}}
print('ID')
for id in a:
    print(id)
    for id in a: 
        for key in a[id]:
            print(key,'=',a[id][key])
print()"""