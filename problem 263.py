# Problem 263 "Engineer's Paradise"
# Nigel Hamilton and Giza Molenaar

from math import sqrt
from time import time

# Finds whether there is triple pair around n
def sexyPrimes(startNum):
    num = startNum-9
    last = num-6
    for n in range(num, num+19, 2):
        dif = n-last
        if prime(n):
            last = n
            if dif != 6:
                return False
        else:
            return False
    return True

# Simple Prime Checker
def prime(testnum):
    prime = True
    div = 3
    maxcheck = sqrt(testnum)
    while prime:
        if testnum % div == 0:
            prime = False
        else:
            div += 2
        if div > maxcheck:
            break
    return prime

# Prime Factorization
def factors(num):
    facts = [1]
    while num % 2 == 0:
        facts.append(2)
        num /= 2
    div = 3
    maxcheck = sqrt(num)
    while div < maxcheck:
        if num % div == 0:
            facts.append(div)
            num = num/div
        else:
            div += 2
    facts.append(num)
    return facts

# Returns whether number is practical
def practical(num):
    facts = factors(num)
    powerOf2 = facts.count(2)
    maxget = 2**(powerOf2+1)
    for i in range(powerOf2):
        facts.remove(2)
    for factor in facts:
        if factor > maxget:
            return False
        maxget *= factor
    return True


def main(n):
    engineersPara = []
    alt = -1
    timeStart = time()
    while len(engineersPara) < 1:
        alt *= -1
        if n%1000000 == 0:
            print(n)
        if sexyPrimes(n):
            if practical(n-8) and practical(n-4) and practical(n) and practical(n+4) and practical(n+8):
                engineersPara.append(n)
        if alt == 1:
            n += 20
        else:
            n += 40
    timeEnd = time()
    timeElapsed = timeEnd-timeStart
    print(round(timeElapsed, 3))
    print(engineersPara)

main(200)
