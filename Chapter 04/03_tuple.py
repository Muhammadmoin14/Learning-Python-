
#! A tuple is an immutable data type in python just like string. The only difference between tuple and list is this difference
#! Immutable means value of tuple cannot change. It is a type of list.

emptyTuple = ()             #? In this way you can make a empty tuple  
print(type(emptyTuple))     #? Result will be <class 'tuple'>


# singleTuple = ("Single Element")      #? It will be a string     
# print(type(singleTuple))              #? Result will be string

singleTuple = ("single element",)       #? Correct way to make a single element tuple
print(type(singleTuple))                #? Result will be <class 'tuple'>

tuple = ("Hamza","bilal","Ahmed",13.4,True,"apple")

# tuple[0] = "Muhammad"                 #? We cannot change the element of tuple


