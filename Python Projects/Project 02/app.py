
#!                           -----PROJECT 2 – THE PERFECT GUESS-----

import random 

def GenerateRandom():
    return random.randint(1, 100)

def UserInput():
    return int(input("Enter your guess: "))

def CheckGuess(User_Guess, randomNum):
    if User_Guess == randomNum:
        print(f"Congratulations! Your guess {randomNum} is correct.")
        return False
    
    elif (User_Guess > randomNum):
        print("Your guess is too high. Try again.")
        return True
    
    else: 
        print("Your guess is too low. Try again.")
        return True


def start_the_Game():
    
    print("\nWelcome to the Perfect Guess Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    randomNum = GenerateRandom()
    Guesses = 0
    Condition = True

    while(Condition == True):
        Guesses =  Guesses + 1
        User_Guess = UserInput()
        Condition = CheckGuess(User_Guess , randomNum)
    
    print(f"You Guess the Corect Answer in {Guesses} Atempt")
    print("Thank you for playing!")


start_the_Game();




