'''Nigel Hamilton
11/3/15
Base converter'''

import isFloat

def findPower(numOrg,base):
    power = 0
    while base**power <= numOrg:
        power += 1
    power -= 1
    return power

def findCoefficient(power,num,base):
    coefficient = 1
    while base**power*coefficient <= num:
        coefficient += 1
    coefficient -= 1
    return coefficient

def userInput(coefLst):
    numOrg = None
    baseOrg = None
    baseFin = None
    while not isFloat.isFloat(baseOrg):
        baseOrg = raw_input("Enter a base up to 16 (10 as default): ") or "10"
        if not isFloat.isFloat(baseOrg):
            print "Input must be number"
        else:
            if eval(baseOrg) > 16 or baseOrg < 2:
                print "Input must be within range"
                baseOrg = None
    baseOrg = eval(baseOrg)
    while not numOrg:
        numOrg = raw_input("Enter a number to convert: ").upper()
        if not numOrg:
            print "Enter a value"
        elif coefLst[baseOrg:] in numOrg:
            print "Input must be within range"
            numOrg = None
    while not isFloat.isFloat(baseFin):
        baseFin = raw_input("Enter a base up to 16 (2 as default): ") or "2"
        if not isFloat.isFloat(baseFin):
            print "Input must be number"
        else:
            if eval(baseFin) > 16 or eval(baseFin) < 2:
                print "Input must be within range"
                baseFin = None
    baseFin = eval(baseFin)
    return numOrg,baseOrg,baseFin

def toBase10(numOrg,baseOrg,coefLst):
    numDummy = numOrg
    numDec = 0
    power = 0
    for i in range(1,len(numOrg)+1):
        numDec += baseOrg**power*coefLst.index(numOrg[-i])
        power += 1
    return numDec,numDummy

def fromBase10(numDec,baseFin,coefLst):
    numFin = ""
    power = findPower(numDec,baseFin)
    while power >= 0:
        if numDec-baseFin**power >= 0:
            coef = findCoefficient(power,numDec,baseFin)
            numDec -= baseFin**findPower(numDec,baseFin)*coef
            coefStr = coefLst[coef]
            numFin += coefStr 
        else:
            numFin += "0"
        power -= 1
    return numFin
    
def main():
    play = "Y"
    coefLst = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while play == "Y":
        numOrg,baseOrg,baseFin = userInput(coefLst)
        numDec,numDummy = toBase10(numOrg,baseOrg,coefLst)
        numFin = fromBase10(numDec,baseFin,coefLst)
        print numDummy,"base-"+str(baseOrg),"=",numFin,"base-"+str(baseFin)
        play = raw_input("Try another number? (Y/N) ").upper() or "N"
        play = play[0]

main()
