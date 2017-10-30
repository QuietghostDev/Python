# Problem 263 "Engineer's Paradise"
# Nigel Hamilton and Giza Molenaar

from math import sqrt
from time import time
from prime import *

# Finds whether there is triple pair around n
def sexyPrimes(startNum):
    num = startNum-9
    primes = 0
    if not miller_rabin(num):
        return False
    last = num-6
    for n in range(num, num+19, 2):
        dif = n-last
        if miller_rabin(n):
            if dif != 6:
                return False
            last = n
            primes += 1
    if primes == 4:
        return True
    else: return False

# Simple Prime Checker
def prime(testnum):
    isPrime = True
    div = 3
    maxCheck = sqrt(testnum)
    while isPrime:
        if testnum % div == 0:
            isPrime = False
        else:
            div += 2
        if div > maxCheck:
            break
    return isPrime

# Prime Factorization the slowest link...
def factors(num):
    facts = []
    while num % 2 == 0:
        facts.append(2)
        num /= 2
    div = 3
    maxCheck = sqrt(num)
    while div < maxCheck:
        if num % div == 0:
            facts.append(div)
            num /= div
        else:
            div += 2
    facts.append(num)
    return facts

# Returns whether number is practical
def practical(num):
    facts = factors(num)
    powerOf2 = facts.count(2)
    maxGet = 2**(powerOf2+1)
    for i in range(powerOf2):
        facts.remove(2)
    for factor in facts:
        if factor > maxGet:
            return False
        maxGet *= factor
    return True


def main(n, iter):
    engineersPara = []
    alt = -1
    timeStart = time()
    # while len(engineersPara) < 1:  # These two lines are interchangable
    for i in range(iter):  # These two lines are interchangable
        alt *= -1
        if n%1000000 == 0:
            print(n)
        if sexyPrimes(n):
            if practical(n-8) and practical(n-4) and practical(n) and practical(n+4) and practical(n+8):
                engineersPara.append(n)
                print("!!!!!", n, "!!!!!")
        if alt == 1:
            n += 20
        else:
            n += 40
    timeEnd = time()
    timeElapsed = timeEnd-timeStart
    print(round(timeElapsed, 3))
    print(engineersPara)
    input()

main(200000000, 100000000)
# startTime = time()
# print(practical(13245687661234600440))
# endTime = time()
# print(endTime-startTime)
# startTime = time()
# print(sexyPrimes(13245687661234600440))
# endTime = time()
# print(endTime-startTime)
