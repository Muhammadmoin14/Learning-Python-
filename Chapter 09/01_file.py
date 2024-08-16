
#! we can read file in python 
#! we can store value in a file using python
#! we can read a file in python using open() function

f = open("file.txt")
data = f.read()                 #? It will read all the data from the file
print(type(data))               #? It will print the type of data which is string
print(data)
f.close()

