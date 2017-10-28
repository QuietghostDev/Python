from math import sqrt

def sexyPrimes(startNum):
    triplePair = []
    num = startNum-9
    dif = 6
    while len(triplePair) < 4:
        if prime(num):
            if dif == 6:
                triplePair.append(num)
            else:
                triplePair = []
        num += 2
        if len(triplePair) == 0:
            dif = 6
        else:
            dif = num-triplePair[-1]
            if (triplePair[0]+9)%20 != 0:
                triplePair = []
    return triplePair

def prime(testnum):
    isPrime = True
    div = 3
    maxcheck = sqrt(testnum)
    while isPrime:
        if testnum % div == 0:
            isPrime = False
        else:
            div += 2
        if div > maxcheck:
            break
    return isPrime
