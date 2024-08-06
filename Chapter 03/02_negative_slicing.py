
#! Introduction to negative slicing in Python 

name = "Moin"

# M  o  i  n   
# 0  1  2  3   #? Postive Index(starts with 0)
# -4 -3 -2 -1  #? Negative Index(starts with -1)

negInd = name[-4 : -1]  #? 0 till 3 is inclusive and 4 is exclusive
print(negInd)           #? Output will be Moi

posInd = name[1:4]      #? Same as negative Index
print(posInd)

#! There also other way to do same task

nameshort = name[:4]    #? It means [0:4]
nameshort = name[0:]    #? It means [0:5(String Lenght)]



