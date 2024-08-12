
#! Argument is a variable which is passed to a function when it is called.
#! The value which is accept by a function is called as argument.
def Greeting(User):                 #? Function Argument (User)
    print(f"Good day {User}")

Greeting("Muhammad")

#! Return in function is used to return a value from a function. 
#! The value which is returned from a function is called as return value.

def avg_func():
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))
    c = int(input("Enter a Number: "))

    avg = (a+b+c)/3
    return avg

Result = avg_func()                              #? Its return a value
print(Result)                                    #? Now we print this value through a variable