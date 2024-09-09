
#! Question 05
#! Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [14,212,36,416,54,62,70,81,99,10]

def greater(a,b):
    if (a>b):
        return a
    else:
        return b
    


result = reduce(greater, l)
print(result)