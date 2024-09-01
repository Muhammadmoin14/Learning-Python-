# Question 05
# Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

n = int(input("Enter a Number"))

result = [i*n for i in range(1,11)]
print(result)

# To write the result in a file named Tables.txt

with open ("table.txt" , "a") as f:
    f.write(f"the table of {n} {str(result)}")
    