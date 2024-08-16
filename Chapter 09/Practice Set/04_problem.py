# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

with open("04_file.txt") as f:
    content = f.read()

content = content.lower()
content = content.replace("donkey", "#####")

with open("04_file.txt","w") as f:

    f.write(content)
