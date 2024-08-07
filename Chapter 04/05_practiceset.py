
# Question 01
# Write a program to store seven markssin a list entered by the user.


fruitTuple = []
fruitTuple.append(input("Enter fruit 1: "))
fruitTuple.append(input("Enter fruit 2: "))
fruitTuple.append(input("Enter fruit 3: "))
fruitTuple.append(input("Enter fruit 4: "))
fruitTuple.append(input("Enter fruit 5: "))
fruitTuple.append(input("Enter fruit 6: "))
fruitTuple.append(input("Enter fruit 7: "))
print(fruitTuple)



# Question 02


studentMark = []
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))
studentMark.append(int(input("Enter marks : ")))

print(f"Students marks are {studentMark}")
studentMark.sort()
print(f"Sorted Students marks are {studentMark}")








# Question 03
# Check that a tuple type cannot be changed in python.

# Check out 03_tuple file



# Question 04
# Write a program to sum a list with 4 numbers.


numList = [1,5,8,9]
print(f"The sum of given list is {sum(numList)}")



# Question 04
# Write a program to count the number of zeros in the following tuple: 

a = (7, 0, 8, 0, 0, 9)
count = a.count(0)
print(f"The number of zeros in the tuple is {count}") 