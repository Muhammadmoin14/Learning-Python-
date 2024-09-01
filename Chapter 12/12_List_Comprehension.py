
l = [3 , 5 , 7 , 9]

sqList = []
for item in l:
    sqList.append(item**2)
    
print(sqList)  # [9, 25, 49, 81]

sqlist2 = [i*i for i in l]
print(sqlist2)  # [9, 25, 49, 81]