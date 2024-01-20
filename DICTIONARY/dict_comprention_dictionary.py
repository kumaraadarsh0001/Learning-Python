#normal dictionary
dict={}
for element in range(20):
    if element%2==0:        #it is condition for dict
        if element%3==0:    #nested condition for dict
            dict[element]=element**2
print(dict)

#this is the dictionary comprention
dict2={element:element**2 for element in range(20) if element%2==0 if element%3==0}
print(dict2)