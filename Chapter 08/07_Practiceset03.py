# Question 07
# Write a python function to remove a given word from a list ad strip it at the same 
# time.

l = ["python", "java", "c++", "c", "javascript"]

def remove(word , list):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

print(remove("c",l))


# Question 08
# Write a python function to print multiplication table of a given number.

def table() :
    n = int(input("Enter the number : "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
table()
