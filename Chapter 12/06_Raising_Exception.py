
# ! We will raise a custom error by using "raise"

a = int(input("Enter a number"))
b = int(input("Enter a number"))
div = a/b

if (b==0):
    raise ZeroDivisionError("You cannot divide by zero")
else:
    print(div)

print("Now If the program is crash It will not run")