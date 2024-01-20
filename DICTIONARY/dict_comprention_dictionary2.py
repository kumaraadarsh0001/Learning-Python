#normal dictionary
dict={}
for element in range(10):
    if element%2==0:        #it is condition for dict
        dict[element]=element
    else:
        dict[element]='invalid'
print(dict)

#this is the dictionary comprention
dict2={element:(element if element%2==0 else 'invalid')for element in range(10)}
print(dict2)