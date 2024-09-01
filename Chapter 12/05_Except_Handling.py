
#! Exception handling is used to handle the runtime errors or exceptions that occur during the execution of a program
#! Exception handling in python is help us to prevent crash of program

#? Syntax of Exception handling in Python

try:
    print()
except Exception as e :
    print(e)

#? Example

try :
    n = int(input("Enter a Number"))    #? If I put rather than integer It will print a error rather than crash a program
except Exception as e :
    print(e)

print("If Program is crash it will not run")
    