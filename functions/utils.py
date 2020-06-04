
import random
import time
import json
import random
from pprint import pprint

from tools.parseInput import Encode
from functions.functionList import functions

def getRandomFlag():

    with open('./questions.json') as fd:
        jd = json.load(fd)
        max = len(jd)-1
        pos = random.randint(0, max)
        flag = jd[ pos  ]['question']
        answer = jd[ pos ]['answer']


    return (flag, answer)

def encrypt(flag, rounds):
    # Encrypt flag
    fn = functions[:-2]
    encryptionAlgorithm = fn[random.randint(0, len(fn)-1)]
    if(encryptionAlgorithm == "CeaserCypher"):
        flag = getattr(Encode, encryptionAlgorithm)(flag, random.randint(10, 40))
    else:
        flag = getattr(Encode, encryptionAlgorithm)(flag)

    if rounds > 1:
        flag = encrypt(flag, rounds - 1)

    return flag

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