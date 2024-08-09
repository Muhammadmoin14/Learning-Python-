
#! Sets is a collection of non repeatative elements. PROPERTIES OF SETS 
#! PROPERTIES OF SETS 
#! 1. Sets are unordered => Element’s order doesn’t matter 
#! 2. Sets are unindexed => Cannot access elements by index 
#! 3. There is no way to change items in sets. 
#! 4. Sets cannot contain duplicate values.



emptySet = set()                    #? In this way you create Empty Set
print(emptySet,type(emptySet))

s = {1,5 ,43 ,"moin",5,5}           #? It doesnt repeat element(5)
print("The set is ",s,type(s))

#! Here are some method of sets

s.add(435)                        #? it add the new value in set
print(s)


s.remove(43)                      #? it remove the value from set
print(s)


# s.pop()                         #? it remove the random value from set
print(s.pop())                    #? it return the remove value from set
print(s)


print(len(s))                     #? it return the length of set


s.clear()                         #? it clear the set
print("Set is now clear",s)



