#!/usr/bin/env python3

import readline
import random
import os
from functions.functionList import functions
from functions.utils import intro, encrypt, getRandomFlag, clear
from tools.colors import colors, bcolors
from tools.parseInput import parseInput
from tools.myCompleter import MyCompleter

startingFlag = None

def incrementLevel(level):
    flag, answer = getRandomFlag()
    level +=1
    encryptedFlag = encrypt(flag, level)
    startingFlag = encryptedFlag
    return level, encryptedFlag, startingFlag, answer

def main():
    clear()

    # intro()

    level = 0

    level, encryptedFlag, startingFlag, answer = incrementLevel(level)


    while(True):
        clear()
        print("{}Level: {}{}\nFlag is: \n\t{}\n".format("\x1b[6;30;42m", level,  '\x1b[0m', encryptedFlag))
        print(secretNumber)
        print("\nAvailable functions are: \n")

        for f in functions:
            if f == "reset" or f == "submit":
                print(">\t{}{}{}".format(colors.RED, str(f), colors.END))
            else:
                print(">\t{}".format(f))

        # choice = input("\n What would you like to do? ")
        completer = MyCompleter(functions)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        choice = input("\n What would you like to do? ")

        if choice.lower() == "submit":
            clear()
            print(("{}Answer the question: {}{}").format(colors.GREEN, colors.END, encryptedFlag))
            ua = input("{}>:\t{}".format(colors.GREEN, colors.END))
            print(ua, answer)
            if ua == answer:
                print("The answer is correct")
                level, encryptedFlag, startingFlag, answer = incrementLevel(level)


        if choice.lower() == "reset":
            encryptedFlag = startingFlag


        encryptedFlag = parseInput(choice, encryptedFlag)


if __name__ == "__main__":
    main()
