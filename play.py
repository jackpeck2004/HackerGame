#!/usr/bin/env python3

import time
from functions.functionList import functions
from tools.parseInput import parseInput

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

flag = "Flag{thisistheflag}"
encryptedFlag = None

def encrypt(flag, rounds):
    for i in range(rounds):
        flag = encrypt(flag, rounds - 1)
    return flag

while(encryptedFlag != flag):
    print("\nAvailable functions are: \n")
    for f in functions:
        print(">\t{}".format(f))
    input("\n What would you like to do? ")
    encryptedFlag = parseInput(input)

