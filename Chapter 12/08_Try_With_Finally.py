
#! Finally block is always run either try run or excrpt run
#! The main used case of finally block is in function. It ignore the return statement (Ex:2) 

#? Example 1:

try :
    n = int(input("Enter a Number"))        
except Exception as e :
    print(e)
# finally:
#     print("It will always run")

print("It will always run as same as finally")
    
    
#? Example 2:

def show():
    try :
        n = int(input("Enter a Number"))
        return 
    except Exception as e :
        print(e)
        return
    finally:                            #? It ignore the return and run 
        print("If try is run sucessfully. It will run")
    
    print("It will not run because of return")
    
show()