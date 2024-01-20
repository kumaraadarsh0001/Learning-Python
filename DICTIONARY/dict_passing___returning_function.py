#Passing and Returning Dictionary to function
def dict(x):
    print('DC:\n',x)
    print('TYPE OF DC:\n',type(x))
    print('ID OF DC:\n',id(x))
    for k in x:
        print(k,'=',x[k])
    return x
dc={101:'kumar aadarsh',102:'lovely boy',103:'flirting king'}
new_dc=dict(dc)
print('NEW_DC:\n',new_dc)
print('TYPE OF NEW_DC:\n',type(new_dc))
print('ID OF NEW_DC:\n',id(new_dc))