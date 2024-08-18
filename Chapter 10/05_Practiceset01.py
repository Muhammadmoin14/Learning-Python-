# Question 01
#  Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

class programmer  :
    company = "Microsoft"

    def __init__(self , name , salary , language): 
        self.name = name
        self.salary = salary
        self.language = language


p1 = programmer("Hafsa" , 85000 , "Python")
print(p1.company , p1.name, p1.salary, p1.language)
p2 = programmer("Ali", 75000, "Java")
print(p2.company , p2.name, p2.salary, p2.language)


# Question 02
# Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 

class calculator :
    def __init__(self, number):
        self.number = number

    def square(self):
        print(self.number**2)

    def cube(self):
        print(self.number**3)

    def squareroot(self):
        print(self.number**0.5)
    


c1 = calculator(5)
c1.square()
c1.cube()
c1.squareroot()

# Question 03
# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?


class sample:
    a = 4

obj = sample()
print(obj.a)            #? It will print class attribute because instance not present
obj.a = 0
print(obj.a)            #? It will print instance attribute because instance present
print(sample.a)         #? It will print class attribute not instance attribute

#! Answer is that class attribute is never change

