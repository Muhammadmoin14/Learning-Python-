# Write a program to find out the line number where python is present from ques 6.



with open("07_log.txt") as f:
    lines = f.readlines()

lineno = 1 

for line in lines:

    if ("python" in line):
        print("Python is present in line ", lineno)
        break
    lineno = lineno + 1
else:
    print("Python is not present")