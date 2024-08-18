
import random

# Question 04
# Add a static method in problem 2, to greet the user with hello. 

class calculator :
    
    @staticmethod
    def greet():
        print("Hello, welcome to the calculator app!")
    
    def __init__(self, number):
        self.number = number

    def square(self):
        print(self.number**2)

    def cube(self):
        print(self.number**3)

    def squareroot(self):
        print(self.number**0.5)
    


c1 = calculator(5)
c1.greet()
c1.square()
c1.cube()
c1.squareroot()

# Question 05
# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class train :

    def __init__(self):
        print("Welcome to Railway!")
        self.trainNo = int(input("Enter train number: "))

    def book(self  , fromStation , toStation):
        print(f"Your ticket has been booked for train number {self.trainNo} from {fromStation} to {toStation}.")

    def status(self ):
        print(f"This train {self.trainNo} is running successful")
    def fare(self  , fromStation , toStation):
        print(f"Your train fare in {self.trainNo} from {fromStation} to {toStation} will be {random.randint(1, 1000)}.")

trainApp = train()
trainApp.book("Karachi", "Islamabad")
trainApp.status()
trainApp.fare("Karachi", "Islamabad")


# Question 06
# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.

# no problem you can give any name 