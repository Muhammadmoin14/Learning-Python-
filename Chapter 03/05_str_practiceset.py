
# Question 01 
# Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 

name = input("Enter your name: ")
print(f"Good Afternoon {name}")




# Question 02 
# Write a program to fill in a letter template given below with name and date. 


letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> ''' 

print(letter.replace("Name","Muhammad Moin").replace("Date","06/08/2024"))

# Question 03
# Write a program to detect double space in a string.

str = "Good  Morning"
print(str.find("  ")) 


# Question 04 
# Replace the double space from problem 3 with single spaces.


print(str.replace("  "," "))




# Write a program to format the following letter using escape sequence 
# characters. 
# letter = "Dear Harry, this python course is nice. Thanks!" 


letter = "Dear Harry,\n\t this python course is nice. \nThanks!" 
print(letter)
