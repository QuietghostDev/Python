import math
import time

def primality():
    testNum = input("Enter Number: ")
    divCount = 1
    sqrtNum = math.sqrt(testNum)
    t1 = time.time()
    while 6*divCount-1 < sqrtNum:
        if testNum%(6*divCount-1) == 0:
            t2 = time.time()
            t3 = t2-t1
            print "Not prime."
            print 6*divCount-1,"is a factor."
            print t3
            break
        elif testNum%(6*divCount+1) == 0:
            t2 = time.time()
            t3 = t2-t1
            print "Not prime."
            print 6*divCount+1,"is a factor."
            print t3
            break
        else:
            divCount += 1
    if 6*divCount-1 >= sqrtNum:
        t2 = time.time()
        t3 = t2-t1
        print "Prime!"
        print t3

primality()
