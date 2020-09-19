# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:51:18 2020

@author: Rashid Hashimzade
"""

import random


computer = 0
player = 0



for abc in range(3) :
    print("Raund : "  +  str(abc + 1))
    computer1 = random.choice("dkq")
    while True :
        select = input("Your choice : ")
        if(select == "d" or select == "k" or select == "q"):
            break
        else :
            print("ERROR!")
            
    print("Computer : " + str(computer1))
    
    
    if(computer1 == select):
        print("Draw!")
    if(computer1 == "d" and select == "k") :
        player = player + 1
        print("You won!")    
    if(computer1 == "q" and select == "d") :
        player = player + 1
        print("You won!")
    if(computer1 == "k" and select == "q") :
        player = player + 1
        print("You won!")
    if(computer1 == "q" and select == "k") :
        computer = computer + 1
        print("You lost!")
    if(computer1 == "k" and select == "d") :
        computer = computer + 1
        print("You lost!")
    if(computer1 == "d" and select == "q") :
        computer = computer + 1
        print("You lost!")
        
        
print("-GAME RESULT-")


if (computer > player ) :
    print("YOU LOST THIS GAME! ")
if(player > computer) :
    print("Congratulations, YOU WON THIS GAME! ")
else :
    print(" DRAW! ")

       
        
        
    
    
    
    