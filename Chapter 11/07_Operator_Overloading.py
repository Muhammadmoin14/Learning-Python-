
class number:

    def __init__(self, num1) :
        self.num1 = num1
    
    def __add__(self, num2) :
        print("Let's add")
        return self.num1 + num2.num1
    

n = number(4)
m = number(3)

print(n + m)