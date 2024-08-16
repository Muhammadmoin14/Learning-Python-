
#! here are some examples of file function in python

file = open("file_function.txt")
data = file.readlines()                 #? it will return list of lines
print(data)
file.close()


file = open("file_function.txt")
line01 = file.readline()                 #? it will return first line
print(line01)
file.close()

#! we do above task with the help of while loop 

file = open("file_function.txt")
readline = file.readline()
while(readline != ""):
    print(readline)
    readline = file.readline()
file.close()
