
class Empolyee:
    a = 1
    

class Programmer(Empolyee):
    b = 2
    
class Manager(Programmer):
    c = 3



EmpolyeeData = Empolyee()
print(EmpolyeeData.a)
# print(EmpolyeeData.b) #? It will not run because it cant contain this attribute

ProgrammerData = Programmer()
print(ProgrammerData.a , ProgrammerData.b)


ManagerData = Manager()
print(ManagerData.a , ManagerData.b , ManagerData.c)

