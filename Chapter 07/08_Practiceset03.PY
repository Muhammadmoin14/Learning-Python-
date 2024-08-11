# Question 07
# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 


for i in range(1,4):
    print("*" * (i*2-1))




# Question 08
# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3

for i in range(1,4):
    print("*" * i)


# Question 09
# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 

n=3
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*" * n ,end = "")
    else:
        print("*", end = "")
        print("  " * (n-2), end = "")
        print("*", end = "")
    print(" ")


# Question 10
# Write a program to print multiplication table of n using for loops in reversed 
# order. 

n = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")