

l = [33 , 54 , 543 , 765]

index = 0
for item in l :
    print(f"The index of {item} is {index}")
    index += 1

#? This can be done by using Enumerate Function

for item , index in enumerate(l):
    print(f"The index of {index} is {item}")