# lst=[2,3,4,5,6]
# if lst:
#     print("not empty")
# else:
#     print("empty")
def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return"You didn't pass any args"

nums=[2,3,4,5]
print(to_power(3,*nums))