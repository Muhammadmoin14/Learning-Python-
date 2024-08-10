
#? Question 01
# Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1, "is the greatest number")
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2, "is the greatest number")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3, "is the greatest number")
else:
    print(num4, "is the greatest number")



#? # Question 02
# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.



Sub1 = int(input("Enter the subject1 marks:"))
Sub2 = int(input("Enter the subject2 marks:"))
Sub3 = int(input("Enter the subject3 marks:"))

#? first calculate total percentage  
totalPercentage = ((Sub1 + Sub2 + Sub3)/300)*100

#? Then check for 40% and at least 33%

if (totalPercentage >= 40 and Sub1>=33 and Sub2>33 and Sub3>33):
    print("You are passed in exams" , totalPercentage)
else:
    print("You are failed in exams" , totalPercentage )



#? Question 03
# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

SpamMessage1 = "Make a lot of money"
SpamMessage2 = "buy now"
SpamMessage3 = "subscribe this"
SpamMessage4 = "click this"

userMessage = input("Enter the message")
if ((SpamMessage1 in userMessage) or (SpamMessage2 in userMessage) or (SpamMessage3 in userMessage) or (SpamMessage4 in userMessage) ):
    print("This is a Spam Message")
else:
    print("Not a Spam message ")


#? Question 04
# Write a program to find whether a given username contains less than 10 
# characters or not.

userInp = input("Enter the username: ")
userlenght = len(userInp)
if(userlenght <=10):
    print("The username is less than 10 characters")
else:
    print("The username is not less than 10 characters")

