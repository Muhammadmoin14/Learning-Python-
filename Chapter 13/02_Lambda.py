
#! Lamda function is a way to create function in shorter way.
#! Function created using an expression using ‘lambda’ keyword.

#? Example 01 : (create square function)

# Normal Function

def square1(a:int):
    return a * a

print(square1(5))            #? Output '25'

# Lamda Function

square = lambda a: a * a
print(square(5))            #? Output '25'

