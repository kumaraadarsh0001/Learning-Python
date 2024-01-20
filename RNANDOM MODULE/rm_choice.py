import random
lst=[10,20,30,40,50,60,70,80,90,100]
#it will choice a number in the list and print randomly
ch=random.choice(lst)
print(ch)
#another choice function in random module
# # import the random module
import random


# declare a list
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
