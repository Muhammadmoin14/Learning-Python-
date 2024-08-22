# Question 04
# Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self , real , imaginary) :
        self.real = real
        self.imaginary = imaginary

    def __add__(self , c2):
        return Complex(self.real + c2.real , self.imaginary + c2.imaginary)
    
    def __mul__(self , c2):
        
        real_part = self.real * c2.real - self.imaginary * c2.imaginary
        imaginary_part = self.real * c2.imaginary + self.imaginary * c2.real
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c = Complex(2, 3)
c2 = Complex(4, 5)
print(c + c2)
print(c * c2)


# Question 05
#  Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.


class vector:

    def __init__(self , i , j , k) :

        self.i = i
        self.j = j
        self.k = k

    def __add__(self , v2):
        return vector(self.i + v2.i , self.j + v2.j , self.k + v2.k)
    
    def __mul__(self , v2):
        return ((self.i * v2.i ) + (self.j * v2.j) + (self.k * v2.k))
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    

v1 = vector(2, 3, 4)
v2 = vector(4, 5, 6)
print(v1 + v2)
print(v1 * v2)