
#! Skip Slicing in String 

#* Example 01:

Alphabet = "abcdefghijklmnopqrstuvwxyz"

sliceSkip = Alphabet[0::5] #? it means [0:26:5]
print(sliceSkip)           #? Output will be 'afkpuz'


#* Example 02: 

counting = "0123456789"
counSkip1 = counting[1:7:3]
print(counSkip1)            #? Output will be '14'

counSkip2 = counting[0:10:2]
print(counSkip2)            #? Output will be '02468'


