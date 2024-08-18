
#! We can not give function under class without self

class Student:
    name = "Muhammad"
    age = 17
    gender = "Male"
    origin = "Pakistan"

    def studentInfo(self):          #? self is a argument  
        print(self.name , self.age , self.gender , self.origin)


dataUser = Student()
dataUser.studentInfo()

#! If we donot want to give argument and we donot need this we used static method
class Student1:
    name = "Muhammad"
    age = 17
    gender = "Male"
    origin = "Pakistan"

    @staticmethod
    def greet():
        print("Hello, World!")

Datastd=Student1() 
Datastd.greet()