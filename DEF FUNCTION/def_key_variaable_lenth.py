#key variable length
from optparse import Values


def add(**num):
    for value in num.items():
        print(value)

add(name="vikash",roll=4848,classes=4,grade=43)