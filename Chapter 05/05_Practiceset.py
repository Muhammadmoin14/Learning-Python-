
#! Question 01
# Write a program to create a dictionary of Urdu words with values as their English 
# translation. Provide user with an option to look it up!

words = {
    "madad": "help",
    "insaf": "justice",
    "qanon": "law",
    "nazam": "poem",
    "zindagi": "life",
    "muhabat": "love"
}

enterWord = input("Enter a Urdu word: ")
print(words.get(enterWord, "Word not found"))

#! Question 02
# Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

sets = set()
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
userInput = sets.add(int(input("Enter a number: ")))
print(f"The {len(sets)} unique number of user are {sets}" )


#! Question 03
# Can we have a set with 18 (int) and '18' (str) as a value in it? 

# set = {18, '18'}
# print(set)                  #? Output: {18, '18'} yes we have set of value of both because of type 



#! Question 04
# What will be the length of following set s: 
se = set() 
se.add(20) 
se.add(20.0) 
se.add('20') # length of s after these operations?
print(len(se)) #? Output: 2 because 20 and 20.0 are same value in set so it count as one value


#! Question 05
# s = {}
# What is a type of s ?
#? Output: dict because it is empty dictionary


#! Question 06
# Create an empty dictionary. Allow 4 friends to enter their favourite language as
# values and use keys as their names. Assume that the names are unique.

favLang = {}

name = str(input("Enter your name: "))
language = str(input("Enter your favourite language: "))
favLang.update({name : language})

name = str(input("Enter your name: "))
language = str(input("Enter your favourite language: "))
favLang.update({name : language})

name = str(input("Enter your name: "))
language = str(input("Enter your favourite language: "))
favLang.update({name : language})

name = str(input("Enter your name: "))
language = str(input("Enter your favourite language: "))
favLang.update({name : language})

print(favLang)