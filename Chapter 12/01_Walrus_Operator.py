
#?                               ------CHAPTER 12 – ADVANCED PYTHON 1------



#* The Walrus Operator allows you to assign values to variables as part of an expression. 


if (n:= len([1,2,3,4,5])) > 3:
    print("Greater than 3")

else :
    print("Lower than 3 ")


                    

if(leng := len("Moin")) > 3:
    print(f"This contain more than 4 character {leng}")