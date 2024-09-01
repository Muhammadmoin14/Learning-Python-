a = 20   #? Global Variable access in all our the program

def func():
    a = 10      #? Local Variable access in specific block
    print(f"Local variable {a}")
    

print(f"Global variable {a}")
func()