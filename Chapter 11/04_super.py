
#! Super is a keyword(method) which is used to run constructor of parent class


class Empolyee:
    
    def __init__(self):
        print("Constructor of Empolyee ")
    
    a = 1

class Programmer(Empolyee):
    
    def __init__(self):
        super().__init__()                          #? It will run constructor of Empolyee class (parent class)
        print("Constructor of Programmer ")
    
    b = 2
    
class Manager(Programmer):

    def __init__(self):
        super().__init__()                          #? It will run constructor of programmer class (parent class)
        print("Constructor of Manager ")
    
    c = 3



# EmpolyeeData = Empolyee()
# print(EmpolyeeData.a)


ProgrammerData = Programmer()
print(ProgrammerData.a , ProgrammerData.b)


ManagerData = Manager()
print(ManagerData.a , ManagerData.b , ManagerData.c)

