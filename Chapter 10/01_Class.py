
#! Class is a blueprint for creating objects. OOPS is a concept in programming that organize your code.
#! It is a way of structuring your code to make it easier to understand and reused.

class User :                #? This is a class
    name = "Muhammad"
    age = 17                #? This is a attribute
    gender = "Male"
    origin = "Pakistan"

dataUser = User()
print(dataUser.name)

dataUser.status = "Student"     #? This is a instance attribute
print(dataUser.name , dataUser.status )


