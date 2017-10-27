from math import sqrt

def sexyPrimes(startNum):
    triplePair = []
    num = startNum-9
    if not prime(num):
        return False
    dif = 6
    while len(triplePair) < 4:
        if prime(num):
            if dif == 6:
                triplePair.append(num)
            else:
                return False
        num += 2
        if len(triplePair) == 0:
            dif = 6
        else:
            dif = num-triplePair[-1]
    return True

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

def factors(num):
    facts = [1]
    while num % 2 == 0:
        facts.append(2)
        num = num/2
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

def practical(num):
    facts = factors(num)
    dd = True
    powerOf2 = facts.count(2)
    maxget = 2**(powerOf2+1)
    for i in range(powerOf2):
        facts.remove(2)
    for factor in facts:
        if factor > maxget:
            dd = False
            break
        else:
            maxget = maxget*factor
    return dd

def main(n):
    engineersPara = []
    alt = -1
    while len(engineersPara) < 1:
        alt *= -1
        if sexyPrimes(n):
            print n
            if practical(n-8) and practical(n-4) and practical(n) and practical(n+4) and practical(n+8):
                engineersPara.append(n)
                print n
        if alt == 1:
            n += 20
        else:
            n += 40
    print engineersPara

main(200)
