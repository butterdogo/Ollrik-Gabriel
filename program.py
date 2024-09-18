import math
import random
import time

import sys
from colorama import Fore, init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream



print(Fore.WHITE + "(",Fore.BLUE + "•",Fore.WHITE + ")", "  ",Fore.WHITE + "(",Fore.BLUE + "•",Fore.WHITE + ")",  sep="")

spelarLiv = 30
datorLiv = 30

datorTärning = 0
spelareTärning = 0

rund = 1

while spelarLiv > 0 and datorLiv > 0:
    
    print(Fore.WHITE + "\nrunda", rund)
    
    datorTärning = random.randint(1,6)
    
    print(Fore.RED + "\nDatorns tärningskast blev:", end=" ")
    time.sleep(2)
    print(datorTärning)
    time.sleep(1)
    print(Fore.WHITE + "\n1 för större, 0 för mindre")
    guessValue = input(Fore.BLUE + "Ditt svar: ")

    
    spelareTärning = random.randint(1,6)
    print("Du slog:", spelareTärning)
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

    time.sleep(0.5)

    if spelarLiv <= 0:
        print(Fore.WHITE + "\nDu dog pucko")
        sys.exit

    if datorLiv <= 0:
        print(Fore.WHITE + "\nDu vann pucko")
        sys.exit


    print(Fore.RED + "\nDator Liv:", datorLiv)
    print(Fore.BLUE + "Spelare Liv:", spelarLiv)

    time.sleep(1)
    
    rund += 1