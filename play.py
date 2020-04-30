#!/usr/bin/env python3

import time

print("Welcome to capture the flag")
time.sleep(1)
print("You will be given a string and from there decode the flag")
time.sleep(1)
print("The flag format is as follows: Flag{xxxxxxx}")
time.sleep(1)
print("You will be given a set of functions you can use")
time.sleep(1)
print("Good Luck.")

flag = "Flag{thisistheflag}"
encryptedFlag = None

functions = ["tomare"]

def encrypt(flag, rounds):
    for i in range(rounds):
        flag = encrypt(flag, rounds - 1)
    return flag

while(encryptedFlag != flag):
    print("Available functions are:")
    for f in functions:
        print(f)
    input("What would you like to do? ")

