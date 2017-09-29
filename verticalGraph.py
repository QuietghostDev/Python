def main():
    f = open("finalWordList.txt",'r')
    fString = f.read().lower().replace("\n","")
    f.close()
    fLength = float(len(fString))
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tupleList = []
    for i in letters:
        letterCount = float(fString.count(i))
        perc = (letterCount/fLength)*100
        tupleList.append((i,perc))
    maximum = findMax(tupleList)
    maxPerc = int(maximum[1]*4)
    for i in xrange(maxPerc,0,-1):
        string = ""
        for j in tupleList:
            percVal = round(j[1]*4)
            if percVal >= i:
                string += j[0]
            else:
                string += " "
            string += "   "
        print string

def findMax(tList):
    maximum = tList[0]
    for i in tList:
        if i[1] > maximum[1]:
            maximum = i
    return maximum

main()
