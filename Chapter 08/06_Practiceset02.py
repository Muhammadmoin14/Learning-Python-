
# Question 05
# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3


def pattern(n):
    if(n==0):
        return 
    else:
        print("*" * n)
        pattern(n-1)

n = int(input("Enter the number : "))
pattern(n)

# Question 06
# Write a python function which converts inches to cms.

def convert(inches):
    cm = inches * 2.54
    return cm

inches = float(input("Enter the inches : "))
print(convert(inches))


