# Question 04
# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:        
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    result = a/b
    print(result)
except ZeroDivisionError as z:
    print("Infinite" , z)

