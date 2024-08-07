
#! Here are some method of list(Array)


#* Example 01

list = ["Hamza","bilal","Ahmed",13.4,True,"apple"]
print(list)

list.append("banana")       #? It adds banana in last of list
print(list) 

list.insert(2,"muhammad")   #? It adds muhammad in given index value(2)
print(list)

# list.pop(4)               #? It removes the given index element
print(list.pop(4))          #? It also return the given index element (13.4)
print(list)

list.remove(True)           #? It remove the given element in list(array)
print(list)


#* Example 02

numbers = [2,212,42,54,666,765,41,3,4,31,577,]
print(numbers)

numbers.sort()              #? It sort number in accesending order
print(numbers)

numbers.reverse()
print(numbers)              #? It reverse the number order


