#this opretion can aply any mode(ex.='r','w','a' etc.)
with open('study3.txt') as file:
    data=file.read()
    print(data)
    print(file.closed)
#after extit with statement file will close autometically
print(file.closed)