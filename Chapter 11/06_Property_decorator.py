class Empolyees:
    
    a = 1
    @classmethod
    def show(cls):
        print(f"This will print the class attribute {cls.a}")

    @property
    def name(self):
        return f"{self.ename} {self.lname}"
    
    @name.setter 
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Empolyees()
e.name = "Muhammad Moin"

print(e.fname)
print(e.lname)