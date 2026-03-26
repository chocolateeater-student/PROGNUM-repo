#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#4.3.2
import numpy as np                        #add module
print("welcome to rock paper scissors! very fair, no cheating- enter your guess")
game=["rock","paper","scissors"]          #list with valid inputs
comp=game[np.random.randint(0,3)]         #assigns a random value from the valid inputs list
print("valid inputs are: rock, paper, scissors")              #instruction
human=input("please eneter your guess- no cheating!")         #asks fo rinput
if human==comp:                                               #checks for  a draw
    print("the results are...")
    print("drumroll please...")
    print("its.... a draw!")
    print(f"computer also guessed {comp} - you know what they say, great minds think alike ;)")
elif (human=="paper" and comp=="rock") or (human=="rock" and comp=="scissors") or (human=="scissors" and comp=="scissors"): #checks for humans victory based on game rules
    print("the results are...")
    print("drumroll please...")
    print("you... actually won? wow i didnt expect that one...")
    print(f"computer guessed {comp}, so you beat it, somehow. congrats ig")
elif human != ("rock" or "paper" or "scissors"):
    print("you think youre very funny, huh? unfortunetely for you that does not beat the computers guess.")      #error message in case of wrong input
else:                                                            #last possibility: loss, prints a loss message
    print("aw, better luck next time :)")
    print("ekhem- looser")

