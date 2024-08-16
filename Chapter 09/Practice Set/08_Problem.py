# Write a program to make a copy of a text file “this. txt” 

with open("08_this.txt") as f:
    data = f.read()

with open("08_copy.txt","w") as f:

    f.write(data)