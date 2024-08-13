from colorama import Fore, Back, Style , init
import random

def computerChoice():
    option = [ "snake", "water", "gun" ]
    randomIndex = random.choice(option)
    return randomIndex

def playerChoice():
    playerInput = input("Enter your choice (Snake, Water, Gun): ")
    if(playerInput == "s" or playerInput == "w" or playerInput == "g"):
        playerOption = {"s" : "snake" ,
                    "w" : "water",
                    "g" : "gun"  }
        playerChoice = playerOption.get(playerInput)
        return playerChoice
    else:
        print("Please enter a valid choice")


computerChoice = computerChoice()
playerChoice = playerChoice()

def start_the_game():
    print("\tWelcome to Snake, Water, Gun Game")
    print("\tSnake vs Water vs Gun") 
    print(f"\tComputer Choice {computerChoice} \n\tPlayer Choice {playerChoice}")



start_the_game();



if(computerChoice == playerChoice):
    print(Fore.GREEN + "It's a tie!")
elif(computerChoice == "snake" and playerChoice == "gun"):
    print(Fore.BLUE + "User win!")
elif(computerChoice == "snake" and playerChoice == "water"):
    print(Fore.RED + "User Lose")
elif(computerChoice == "water" and playerChoice == "snake"):
    print(Fore.BLUE + "User Win!")
elif(computerChoice == "water" and playerChoice == "gun"):
    print(Fore.RED + "User Lose!")
elif(computerChoice == "gun" and playerChoice == "snake"):
    print(Fore.RED + "User Lose!")
elif(computerChoice == "gun" and playerChoice == "water"):
    print(Fore.BLUE + "User Win!")


