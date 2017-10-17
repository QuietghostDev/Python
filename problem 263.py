from math import sqrt

def main():
    engineerNums = [3]
    num = 5
    dif = 6
    while len(engineerNums) < 4:
        if prime(num):
            if dif == 6:
                engineerNums.append(num)
            else:
                engineerNums = []
        num += 2
        if len(engineerNums) == 0:
            dif = 6
        else:
            dif = num-engineerNums[-1]
    print engineerNums

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
    print(maxcheck)
    while div < maxcheck:
        if num % div == 0:
            facts.append(div)
            num = num/div
        else:
            div += 2
    facts.append(num)
    return facts

main()
