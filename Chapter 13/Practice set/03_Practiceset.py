
#! Question 03
#!  A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

list = [str(7*i) for i in range(1,11)]

result = "\n".join(list)
print(result)