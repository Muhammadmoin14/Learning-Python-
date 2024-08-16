# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 

import random

def gamefunc():
    
    print("Playing the game...")
    
    score = random.randint(1, 10)
    
    print(f"Your score is {score}")

    with open("hiScore.txt") as f :
        hiScore = f.read()
        if(hiScore != ""):
            hiScore = int(hiScore)
        else:
            hiScore = 0   
        
        if(hiScore < score or hiScore == ""):
            with open("hiScore.txt", "w") as f :    
                f.write(str(score))
    
    return score

gamefunc()
