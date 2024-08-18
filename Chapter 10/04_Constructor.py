
#! __init__() is a special method which is first run as soon as the object is created. 
#! __init__() method is also known as constructor. 
#! It takes ‘self’ argument and can also take further arguments.

class Student:
    name = "Muhammad"
    age = 17
    gender = "Male"
    origin = "Pakistan"

    def __init__(self , name , age , gender , origin):                         #? It is automatically called
        print("It is automatic execute")
        self.name = name
        self.age = age
        self.gender = gender
        self.origin = origin


    def studentInfo(self):          #? self is a argument  
        print(self.name , self.age , self.gender , self.origin)


dataUser = Student("Hafsa" , 22 , "Female" , "Indian")          #? It is now change and now everytime you have to give parameter
print(dataUser.name , dataUser.age, dataUser.gender, dataUser.origin)

