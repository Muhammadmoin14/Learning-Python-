
#! @classmethod decorator is used to run class attribute rather than instance attribute.

class Empolyee:
    
    a = 1

    def show(self):
        print(f"This will print the instance attribute {self.a}")

e = Empolyee()
e.a = 45            #? This is instance attribute and this will print
e.show()            #? Output was 45 


class Empolyees:
    
    a = 1
    @classmethod
    def show(cls):
        print(f"This will print the class attribute {cls.a}")

e = Empolyees()
e.a = 45            #? This is instance attribute but not print
e.show()            #? Output was 1 because class method is used


