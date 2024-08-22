# Question 06
#  Write __str__() method to print the vector as follows: 
# 7i + 8j +10k  
# Assume vector of dimension 3 for this problem.

class vector : 

    def __init__(self ,i ,j ,k) :
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):

        print(f"{self.i}i + {self.j}j + {self.k}k")


v1 = vector(7, 8, 10)
v1.__str__()            #? Print the vector in vector form 


# Question 07
# Override the __len__() method on vector of problem 5 to display the dimension of the 
# vector.

class vector : 

    def __init__(self , l) :
        self.l = l 
    
    def __len__(self):

        print (len(self.l))

v2 = vector([7, 8, 10])
v2.__len__()                #? Print the lenght of vector

