from random import *

def witness(numTest):
    div = 3
    sqrtNum = numTest**0.5
    if (numTest%2 == 0):
        return False
    while (div <= sqrtNum):
        if (numTest%div == 0):
            return False
        else:
            div += 2
    return True
	
def fermat(numTest):
    div = 0
    acc = 20
    while (div < acc):
        primeMod = randint(100, 10000)
        while (witness(primeMod) == False):
            primeMod = randint(100, 10000)
        if (pow(primeMod, numTest-1, numTest) == 1):
            div += 1
        else:
            div = 0
            break
    if (div == acc):
        return True
    return False

