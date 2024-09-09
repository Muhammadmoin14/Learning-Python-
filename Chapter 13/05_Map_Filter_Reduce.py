

#!               ----- MAP FUNCTION -----

num = [1, 2, 3, 4, 5]           #? A list of numbers

sqrFunc = lambda n: n*n         #? square function
sqr = map(sqrFunc , num)        #? Map apply sqr function to each list item
sqrList = list(sqr)             #? Convert the output into list
print(sqrList)                  #? Print the Output [1, 4, 9, 16, 25]


#!               ----- FILTER FUNCTION -----

def even(n):                    #? even function
    if n%2 == 0:
        return True
    else:
        return False
    
evenList = filter(even , num)   #? Filter out the even number which satisfy the condition of if-block
print(list(evenList))           #? Convert list and print Output [2, 4]


#!               ----- REDUCE FUNCTION -----

from functools import reduce

sumFunc = lambda a,b: a+b      #? Sum function
sumNum = reduce(sumFunc , num) #? Reduce apply sum function to all list item 
print(sumNum)                  #? Print the Output 15


mulFunc = lambda a,b:a*b       #? Multipication Function
mulNum = reduce(mulFunc , num) #? Reduce apply mul function to all list item
print(mulNum)                  #? Print the Output 120. It give factorial of last number

