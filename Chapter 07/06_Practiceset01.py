
# Question 01
# Write a program to print multiplication table of a given number using for loop.


number = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")


# Question 02
# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 

l = ["Moin", "Samma", "Sarim", "Raffay"] 

for name in l :
    if(name.startswith("S")):
        print(f"Salam {name}")


# Question 03
# Attempt problem 1 using while loop. 

number = int(input("Enter the number :"))

j = 1
while (j<=10):
    print(f"{number} x {j} = {number*j}")
    j += 1

# Question 04
# Write a program to find whether a given number is prime or not.

number = int(input("Enter the number :"))

for i in range(2,number):
    if(number%i == 0):
        print (f"{number} is not a prime number")
        break;
else:
    print(f"{number} is a prime number")

