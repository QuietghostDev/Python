def sortBy(tup):
    return tup[1]

def openFile(fileName, mode):
    f = open(fileName, mode)
    return f

def main():
    f = openFile("Quotes","r")
    quoteList = f.readlines()
    f.close()
    tupleList = []
    for i in quoteList:
        quote = i[:i.index("%")]
        name = i[i.index("%")+1:]
        tupleList.append((quote, name))
    print tupleList[:2]
    tupleList.sort(key = sortBy)
    print tupleList[:2]
    f = openFile("Quotes","w")
    for i in tupleList:
        f.write(i[0]+"%"+i[1])
    f.close()

main()
    
