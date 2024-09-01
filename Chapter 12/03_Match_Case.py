#               ------ Match Case ------

#! It is just like switch statement in C++ or Javascript
#! Those statement which match the case will run 

#? Syntax of Match_Case in Python

value = 1
    
match value:
    case 1 :
        print("Value Match")

#? Example:

def http_status(status : int): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _:                                             #? Default value  
            return "Unknown status" 
# Usage 
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status  