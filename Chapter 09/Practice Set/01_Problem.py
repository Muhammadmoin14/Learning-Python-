# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("01_poem.txt") as f:
    data = f.read()
    if("twinkle" in data):
        print("Yes, twinkle is present")
    else:
        print("No, twinkle is not present")
