# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:30:53 2023

@author: andrz
"""

import random
import time

print("""
      
      Rock - Paper - Scissors Game
      
      Please choose one of them 
      
      1 - Rock
      2 - Paper
      3 - Scissors
      
      Rules
      
      1 - Rock beats Scissors
      2 - Paper beats Paper
      3 - Scissors beats Paper

      """)

while True:
    
    User_1 = int(input("Your choice: "))
    
    if User_1 == 4:
        print("Game over")
        break
    
    elif User_1 >=5:
        print("Please Choose 1 to 4")
        
    else:
        Game = {1:"Rock", 2:"Paper",3:"Scissors"}
        
        AI_1 = random.randint(1,3)
        
        AI = Game.get(AI_1)
        User = Game.get(User_1)
        
        if User == "Rock" and AI == "Scissors":
            time.sleep(0.1)
            print("I choose scissiors, u WIN!")
        
        elif User == "Paper" and AI == "Rock":
            time.sleep(0.1)
            print("I choose Rock, u WIN!")
        
        elif User == "Scissors" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, u WIN!")
        
        elif User == "Paper" and AI == "Scissors":
            time.sleep(0.1)
            print("I choose scissors, u LOSE!")
        
        elif User == "Scissors" and AI == "Rock":
            time.sleep(0.1)
            print("I choose rock, u LOSE!")
        
        elif User == "Rock" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, u LOSE!")
        
        else:
            print("Draw, let's go again!")
        
        
        
    