
#? Question 05
# Write a program which finds out whether a given name is present in a list or not. 

list = ["muhammad","moin","bilal","huzaifa","moiz","hamza"]

name = input("Enter the name to check: ")

if(name in list):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

#? Question 06
# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F


marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "Ex"
elif(marks >= 80):
    grade = "A"
elif(marks >= 70):
    grade = "B"
elif(marks >= 60):
    grade = "C"
elif(marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is " + grade)

#? Question 07
# Write a program to find out whether a given post is talking about 'moin' or not.

post = input("Enter the post: ")

if ("Moin".lower() in post.lower()):
    print("The post is talking about Moin") 
else:
    print("The post is not talking about Moin")

