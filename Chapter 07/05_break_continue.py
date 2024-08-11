
#! Break exit the loop immediately

#! Imagine you have a list of numbers, and you're looking for the first number 
#! that is divisible by 5. Once you find it, you want to stop looking and print that number.

numbers = [3, 8, 12, 15, 21, 25, 30]

for i in numbers :
    if i % 5 == 0:
        print("Found the number which is divisible by 5 is : ",i)
        break            #? Stop the loop once we find a number divisible by 5

#! Continue skips the current iteration of the loop
#! you want to skip over all the numbers that are divisible
#! by 3 and only print the ones that are not divisible by 3.


numbers = [3, 8, 11, 15, 21, 25, 30]

for i in numbers :
    if i % 3 == 0:
        continue
    print("Not divisible by 3 : ",i)

#! pass is a null statement in python.
#! It instructs to “do nothing”.

