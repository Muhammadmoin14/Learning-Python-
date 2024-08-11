
# Question 05
# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number : "))

i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i += 1    
print(sum)


# Question 06
# Write a program to calculate the factorial of a given number using for loop.

number = int(input("Enter the number : "))

fact = 1


for i in range(1,number+1):
    fact = fact * i
    
    
print(f"The factorial of {number} is : {fact}")
