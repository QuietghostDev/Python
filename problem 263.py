from math import sqrt

def main():
    firstprime = 3
    while found = false:


def prime(testnum):
    prime = True
    div=3
    maxcheck = sqrt(testnum)
    while prime:
        if testnum%div = 0:
            prime = False
        else:
            div += 2
        if div>maxcheck:
            break
    return prime

def factors(num):
    facts = [1]
    while num%2 == 0:
        facts.append(2)
        num =num/2
    div = 3
    maxcheck = sqrt(num)
    while div < maxcheck:
        if num%div == 0:
            facts.append(div)
            num = num/div
        else:
            div+=2
