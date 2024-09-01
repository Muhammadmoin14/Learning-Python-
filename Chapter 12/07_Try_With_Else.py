

#! Syntax of try with else

#* try: 
# Somecode 
#* except: 
# Somecode 
#* else: 
# Code                  #? This is executed only if the try was successful         

#! Example

try :
    n = int(input("Enter a Number"))        #? If I put rather than integer It will print a error rather than crash a program
except Exception as e :
    print(e)
else:
    print("If try is run sucessfully It will run")
    
    