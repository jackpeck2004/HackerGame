#!/usr/bin/env python3

import readline
import random
import os
from functions.functionList import functions
from functions.utils import intro, encrypt, getRandomFlag
from tools.colors import colors
from tools.parseInput import parseInput
from tools.myCompleter import MyCompleter

startingFlag = None

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()
    # flag = 'lacapitalediitalia'
    flag, answer = getRandomFlag()

    encryptedFlag = None
    level = 1

    encryptedFlag = encrypt(flag, level)
    startingFlag = encryptedFlag

    while(True):
        print("\nFlag is: \n\t{}\n".format(encryptedFlag))
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
            print(("{}Answer the question: {}{}").format(colors.GREEN, colors.END, encryptedFlag))
            ua = input("{}>:\t{}".format(colors.GREEN, colors.END))
            print(ua, answer)
            if ua == answer:
                print("The answer is correct")

        if choice.lower() == "reset":
            encryptedFlag = startingFlag


        encryptedFlag = parseInput(choice, encryptedFlag)


if __name__ == "__main__":
    main()
