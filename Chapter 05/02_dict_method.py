studentMarks = {
#   "key"     : "value",
    "Muhammad" : 98,
    "Moin" : 96,
    "ahmed" : 78,
    "bilal" : 32

}


#! Here are some method of dictionary


print(studentMarks.keys())      #? This will print all the keys of the dictionary
print(studentMarks.items())     #? This will print list (tuple) of the dictionary
print(studentMarks.values())    #? This will print all the values of the dictionary



studentMarks.update({"Muhammad" : 100})     #? This will update the value of the key 
studentMarks.update({"Ali" : 88})           #? also add the new key value pair if the key is not present in the dictionary
print(studentMarks)

# studentMarks.clear()                      #? This will clear the dictionary
# studentMarksCopy = studentMarks.copy()    #? This will create a copy of the dictionary




print(studentMarks.get("Muhammad"))         #? This will print the value of the key
print(studentMarks["Muhammad"])             #? This will also print the value of the key

#! Difference between .get() and [] in dictionary

# print(studentMarks.get("Alee"))              #? If the key is not present in the dictionary then it will return None
# print(studentMarks["Alee"])                  #? If the key is not present in the dictionary then it will raise an error

#! pop() and popitem() method in dictionary


# studentMarks.pop("Moin")                     #? This will remove the key-value pair from the dictionary
print(studentMarks.pop("Moin"))                #? This will return the value of remove key from the dictionary
print(studentMarks)

studentMarks.popitem()                         #? This will remove the last key-value pair from the dictionary
print(studentMarks.popitem())                  #? This will return the last key-value pair from the dictionary
print(studentMarks)

