# Inheritance is a way of creating a new class from an existing class.

class Employee:                     #? Base class or Parent class
    companyName = "Google"
    name = "default name"
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the company is {self.companyName}")


# class programmer :
#     companyName = "Youtube"
#     name = "deafault name" 
#     def showDetails(self):
#         print(f"The name of the employee is {self.name} and the company is {self.company}")

#     def showLanguages(self):
#         print(f"The programmer is perfect in this language {self.language}")


#! Instead of doing this we can use inheritance like this: 

class programmer(Employee):         #? Derived class or Child class
    companyName = "Youtube"
    language = "python"
    def showLanguages(self):
        print(f"The programmer is perfect in this language {self.language}")


a = Employee()
b = programmer()
print(a.companyName , b.companyName)

b.showDetails()
b.showLanguages()




