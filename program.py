#   179  mkdir code
#   180  cd code
#   181  mkdir te22-tp1-intro/
#   182  cd te22-tp1-intro
#   183  code .

import math
import random

spelarLiv = 30
datorLiv = 30

datorTärning = 0
spelareTärning = 0

while spelarLiv > 0 and datorLiv > 0:
    datorTärning = random.randint(1,6)
    print("Datorns tärningskast blev:")
    print(datorTärning)

    guessValue = input("1 för större, 0 för mindre")
    print(guessValue)
    
    spelareTärning = random.randint(1,6)
    print(spelareTärning)
#allt är Henriks fel kanske
    if guessValue == "1":
        if spelareTärning > datorTärning:
            datorLiv -= spelareTärning
          
        else: 
            spelarLiv -= spelareTärning
    
    if guessValue == "0":
        if spelareTärning < datorTärning:
            datorLiv -= spelareTärning
        else:
            spelarLiv -= spelareTärning

    if spelareTärning == datorTärning:
        spelarLiv -= spelareTärning * 2


    if spelarLiv <= 0:
        print("Du dog pucko")

    if datorLiv <= 0:
        print("Du vann pucko")
        

    print("Dator Liv: ", datorLiv)
    print("Spelare Liv: ", spelarLiv)

    
