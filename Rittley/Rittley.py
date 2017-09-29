'''
The Rittley
Grammar
'''

def verbFile():
    fl = open("C:/Users/Nigel/Documents/My Programs/Python/Rittley/verbList.txt","r")
    verbList = fl.read().split("\n")
    return verbList

def nounFile():
    fl= open("C:/Users/Nigel/Documents/My Programs/Python/Rittley/nounList.txt", "r")
    nounList = fl.read().split("\n")
    return nounList

def prepFile():
    fl=open("C:/Users/Nigel/Documents/My Programs/Python/Rittley/preposition list.txt", "r")
    prepList = fl.read().split("\n")
    return prepList

def pastFile():
    fl=open("C:/Users/Nigel/Documents/My Programs/Python/Rittley/pastPassive.txt", "r")
    pastList = fl.read().split("\n")
    return pastList

def sentence(fileWordList,count,nounList,verbList,pastList,prepList,verbIndex,verb):
    plural=0
    prep=0
    for i in fileWordList:
        if i=="your":
            fileWordList[fileWordList.index(i)] = "the"
            count+=1
        if i in verbList:
            verbIndex = fileWordList.index(i)
            newVerb = verbList[verbIndex]
            verb=verbList.index(i)
        elif i in prepList and fileWordList.index(i)!=verbIndex+1:
            prep=1
            prepIndex = fileWordList.index(i)
            if (plural==0):
                fileWordList.insert(prepIndex, "was ")
            else:
                fileWordList.insert(prepIndex, "were ")
            fileWordList.insert(prepIndex+1, pastList[verb])
            fileWordList.pop(verbIndex)
            break
        elif i in prepList and fileWordList.index(i)==verbIndex+1:
            andindex=fileWordList.index("and")
            if (plural==0):
                fileWordList.insert(andindex, "was")
            else:
                fileWordList.insert(andindex, "were")
            fileWordList.insert(andindex+1,pastList[verb])
            fileWordList.insert(andindex+2,fileWordList[verbIndex+1])
            fileWordList.pop(verbIndex)
        elif i not in nounList:
            if i[-1]=="s":
                plural=1
        elif count==len(fileWordList) and prep==0:
            if (plural==0):
                fileWordList.append("was")
            else:
                fileWordList.append("were")
            fileWordList.append(pastList[verb])
            fileWordList.pop(verbIndex)
    return fileWordList,count

def findVerb():
    fl2=raw_input("enter a lab procedure")
    newFile=fl2.lower().split(". ")
    verbList = verbFile()
    nounList = nounFile()
    prepList = prepFile()
    pastList = pastFile()
    for j in newFile:
        fileWordList=j.strip(".").strip(",").strip("?").strip("(").strip(")").split()
        plural=0
        count=0
        prep=0
        for i in fileWordList:
            if "if" in fileWordList:
                fileWordList=[""]
                break
            if i=="your":
                fileWordList[fileWordList.index(i)] = "the"
            count+=1
            if i in verbList:
                verbIndex = fileWordList.index(i)
                newVerb = verbList[verbIndex]
                verb=verbList.index(i)
            elif i in prepList and fileWordList.index(i)!=verbIndex+1:
                prep=1
                prepIndex = fileWordList.index(i)
                if (plural==0):
                    fileWordList.insert(prepIndex, "was")
                else:
                    fileWordList.insert(prepIndex, "were")
                if prepIndex+1 >= len(fileWordList):
                    fileWordList.append(pastList[verb])
                else:
                    fileWordList.insert(prepIndex+1, pastList[verb])
                    fileWordList.pop(verbIndex)
                if "and" in fileWordList and fileWordList.index("and")>prepIndex:
                    andindex=fileWordList.index("and")
                    fileWordList[andindex+1:],count=sentence(fileWordList[andindex+1:],count,nounList,verbList,pastList,prepList,verbIndex,verb)
                break
            elif i in prepList and fileWordList.index(i)==verbIndex+1 and "and" in fileWordList:
                andindex=fileWordList.index("and")
                if (plural==0):
                    fileWordList.insert(andindex, "was")
                else:
                    fileWordList.insert(andindex, "were")
                fileWordList.insert(andindex+1,pastList[verb])
                fileWordList.insert(andindex+2,fileWordList[verbIndex+1])
                fileWordList.pop(fileWordList.index(i)-1)
                fileWordList.pop(fileWordList.index(i))
                if "and" in fileWordList and fileWordList.index("and")>prepIndex:
                    andindex=fileWordList.index("and")
                    fileWordList[andindex+1:],count=sentence(fileWordList[andindex+1:],count,nounList,verbList,pastList,prepList,verbIndex,verb)
                break
                
            elif i not in nounList:
                if i[-1]=="s":
                    plural=1
            elif count==len(fileWordList) and prep==0:
                if (plural==0):
                    fileWordList.append(" was")
                else:
                    fileWordList.append(" were")
                fileWordList.append(pastList[verb])
                fileWordList.pop(verbIndex)
        newFile[newFile.index(j)]=fileWordList
    final=""
    for i in newFile:
        for j in i:
            final=final+" "+j
    print final

findVerb()
            
