
#! If we want to open a file but not close we used with statement

with open("file.txt") as f:
    print(f.read())

#! And we dont need to use f.close()

with open ("file_write.txt") as f:
    print(f.read())