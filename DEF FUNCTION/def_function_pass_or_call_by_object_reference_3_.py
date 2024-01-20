# IFBA=INSIDE FUNCTION BEFOR APPEND
# IFAA=INSIDE FUNCTION AFTER APPEND
# BCF=BEFOR CALLING Function
# ACF=AFTER CALLING FUNCTION
def val(lst):
    print("IFBA",lst,id(lst))
    lst=[11,12,13]
    print("IFAA",lst,id(lst))

lst=[1,2,3]
print("BCF",lst,id(lst))
val(lst)
print("ACF",lst,id(lst))
