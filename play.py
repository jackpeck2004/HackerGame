#!/usr/bin/env python3

import time
import readline
import random
from functions.functionList import functions
from tools.colors import colors
from tools.parseInput import parseInput
from tools.parseInput import Encode
from tools.myCompleter import MyCompleter


def intro():
    print("Welcome to capture the flag")
    time.sleep(1)
    print("You will be given a string and from there decode the flag")
    time.sleep(2)
    print("The flag format is as follows: Flag{xxxxxxx}")
    time.sleep(2)
    print("You will be given a set of functions you can use")
    time.sleep(1)
    print("Good Luck.")
    time.sleep(2)

startingFlag = None

def encrypt(flag, rounds):
    # Encrypt flag
    fn = functions[:-2]
    encryptionAlgorithm = fn[random.randint(0, len(fn)-1)]
    if(encryptionAlgorithm == "CeaserCypher"):
        flag = getattr(Encode, encryptionAlgorithm)(flag, random.randint(1, 40))
    else:
        flag = getattr(Encode, encryptionAlgorithm)(flag)

    if rounds > 1:
        flag = encrypt(flag, rounds - 1)

    return flag


def main():
    # flag = 'la capitale di Italia?'
    # flag = 'la_capitale_di_Italia?'
    flag = 'lacapitalediitalia'
    # flag = "bGEgY2FwaXRhbGUgZGkgSXRhbGlhY2lhb2NpYW9jaWFv"
    encryptedFlag = None
    # answer = "roma"
    level = 1

    encryptedFlag = encrypt(flag, level)
    startingFlag = encryptedFlag

    while(True):
        print("\nFlag is: \n\t{}\n".format(encryptedFlag))
        print("\nAvailable functions are: \n")

        for f in functions:
            if f == "reset" or f == "submit":
                print(">\t{}{}{}".format(colors.BOLD, str(f), colors.END))
            else:
                print(">\t{}".format(f))

        # choice = input("\n What would you like to do? ")
        completer = MyCompleter(functions)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        choice = input("\n What would you like to do? ")

        '''
        if choice.lower() == "submit":
            # check della risposta
            print("Answer {}".format(encryptedFlag))

        '''

        if choice.lower() == "reset":
            encryptedFlag = startingFlag


        encryptedFlag = parseInput(choice, encryptedFlag)


if __name__ == "__main__":
    main()
