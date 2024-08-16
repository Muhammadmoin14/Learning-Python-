#  Write a program to wipe out the content of a file using python. 

with open("10_file.txt") as f:
    content = f.read()

content = ""

with open("10_file.txt", "w") as f:
    f.write(content)