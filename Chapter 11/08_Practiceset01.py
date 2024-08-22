
# Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector.

class twodvector:
    
    def __init__(self ,i,j) :
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")

class threedvector(twodvector):
    
    def __init__(self, i, j, k) :
        
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


twoDimension = twodvector(1, 2)
threeDimension = threedvector(1, 2, 3)

twoDimension.show()
threeDimension.show()


# Question 02
# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 


class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    
    @staticmethod
    def bark():
        print("Bow Bow !")

d = dog()
d.bark()


# Question 03
# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.


class Employee:

    salary = 1000
    increment = 30

    @property
    def afterIncrementSalary(self):
        return self.salary + self.salary * (self.increment / 100)

    @afterIncrementSalary.setter
    def afterIncrementSalary(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

emp = Employee()
print(emp.afterIncrementSalary)  # Prints the salary after increment

emp.afterIncrementSalary = 1300  # Sets the increment based on the desired salary
print(emp.increment)  # Prints the new increment percentage
