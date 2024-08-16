# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.


def tablefunc():
    for n in range(2,21):
        with open(f"03_table/table{n}.txt", "w") as f :
            for i in range(1,11 ):
                table = f"\n {n} x {i} = {n*i}"
                table = str(table)
                f.write(table)

tablefunc()