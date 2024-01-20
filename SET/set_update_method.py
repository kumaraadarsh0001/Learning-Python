x={'python',985,4560}
y=set()
z=set()
print(id(x))
print('X set=',x,'      Y set=',y,'     Z set=',z)      #it can print empty set
a=['Boy',10,12.12,'Lovely']
x.update(a)
y.update({'Aadrsh',12,14.12,'Kumar'})
z.update(("Flirting",34,20.4,'King'))
print("after add a list in set  X    = ",x)
print("after add a set in set  Y     = ",y)
print("after add a tiple in set  Z   = ",z)
print(id(x))