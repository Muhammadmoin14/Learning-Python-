
class Employee:
    language = "Python"
    salarly = 85000
    status = "Active"

emp1 = Employee()       #? Instance attributes, take preference over class attributes
emp1.language = "Typescript" 
print(emp1.language , type(emp1.language))
