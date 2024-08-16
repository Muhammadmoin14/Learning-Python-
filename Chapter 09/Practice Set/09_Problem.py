# Write a program to find out whether a file is identical & matches the content of 
# another file. 

with open("08_this.txt") as f:
    data1 = f.read()

with open("08_copy.txt") as f:
    data2 = f.read()

if(data1 == data2):
    print("Files are identical")
else:
    print("Files are not identical")