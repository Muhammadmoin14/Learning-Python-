# Write a program to mine a log file and find out whether it contains ‘python’. 

with open("06_log.txt") as f:
    data = f.read()

if ("python" in data):
    print("Python is present")
else:
    print("Python is not present")