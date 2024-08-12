
# Question 01
# Write a program using functions to find greatest of three numbers. 

def greatNum():
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))

    if(a>b and a>c):
        print("The greatest number is : ",a) 
    elif(b>a and b>c):
        print("The greatest number is : ", b)
    else:
        print("The greatest number is : ", c)

greatNum()

# Question 02
# Write a python program using function to convert Celsius to Fahrenheit.
def cel_to_fra(C):
    
    F = (9/5 * C) + 32
    print("The temperature in Fahrenheit is : ", F)

C = int(input("Enter the temperature in Celsius : "))
cel_to_fra(C)


# Question 04
# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n == 1:
        return 1
    else:
        result = n + sum(n-1)    
        return result

n = int(input("Enter the number : "))
print(f"The sum of first {n} natural numbers is :  {sum(n)}")


