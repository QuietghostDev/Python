'''Nigel Hamilton
11/3/15
Base converter'''

import isFloat

def findPower(numDec,base):
    power = 0
    while base**power <= numDec:
        power += 1
    power -= 1
    return power

def findCoefficient(power,numDec,base):
    coefficient = 1
    while base**power*coefficient <= numDec:
        coefficient += 1
    coefficient -= 1
    return coefficient

def userInput():
    numDec = None
    base = None
    while not isFloat.isFloat(numDec):
        numDec = raw_input("Enter a number to convert: ")
        if not numDec:
            print "Enter a value"
        elif not isFloat.isFloat(numDec):
            print "Input must be number"
    numDec = eval(numDec)
    while not isFloat.isFloat(base):
        base = raw_input("Enter a base up to 16 (2 as default): ") or "2"
        if not isFloat.isFloat(base):
            print "Input must be number"
        else:
            if eval(base) > 16 or eval(base) < 2:
                print "Input must be within range"
                base = None
    base = eval(base)
    return numDec,base

def main():
    play = "Y"
    coefLst = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while play == "Y":
        numDec,base = userInput()
        numDummy = numDec
        numFin = ""
        power = findPower(numDec,base)
        while power >= 0:
            if numDec-base**power >= 0:
                coef = findCoefficient(power,numDec,base)
                numDec -= base**findPower(numDec,base)*coef
                coefStr = coefLst[coef]
                numFin += coefStr
            else:
                numFin += "0"
            power -= 1
        print numDummy,"base-10 =",numFin,"base-"+str(base)
        play = raw_input("Try another number? (Y/N) ")[0].upper()

main()
