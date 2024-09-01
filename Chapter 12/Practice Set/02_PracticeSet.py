# Question 02
#  Write a program to print third, fifth and seventh element from a list using enumerate function.

List = [21, 31 , 53, 63 ,24, 41 , 76, 89 ,57]

for index , item in enumerate(List):
    if index == 2 or index == 4 or index == 6 :
        print(item)