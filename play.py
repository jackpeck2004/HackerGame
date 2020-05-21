#!/usr/bin/env python3

import time
import random
from functions.functionList import functions
from tools.parseInput import parseInput
from tools.parseInput import Encode


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


def encrypt(flag, rounds):
    # Encrypt flag
    encryptionAlgorithm = functions[random.randint(0, len(functions)-1)]
    if(encryptionAlgorithm == "CeaserCypher"):
        flag = getattr(Encode, encryptionAlgorithm)(flag, random.randint(1, 40))
    else:
        flag = getattr(Encode, encryptionAlgorithm)(flag)

    if rounds > 1:
        flag = encrypt(flag, rounds - 1)

    return flag


def main():
    flag = 'la capitale di Italia?'
    # flag = "bGEgY2FwaXRhbGUgZGkgSXRhbGlhY2lhb2NpYW9jaWFv"
    encryptedFlag = None
    # answer = "roma"
    level = 0

    encryptedFlag = encrypt(flag, level)

    while(True):
        print("\nFlag is: \n\t{}\n".format(encryptedFlag))
        print("\nAvailable functions are: \n")

        for f in functions:
            print(">\t{}".format(f))

        choice = input("\n What would you like to do? ")
        if choice.lower() == "submit":
            # check della risposta
            print("Answer {}".format(encryptedFlag))
            pass

        encryptedFlag = parseInput(choice, encryptedFlag)


if __name__ == "__main__":
    main()
