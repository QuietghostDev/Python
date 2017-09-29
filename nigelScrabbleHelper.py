'''Nigel Hamilton
Scrabble Helper
3/9/15'''

def main():
    f = open("C:\\Users\\Nigel\\Documents\\My Programs\\Python\\newWordList.txt", "r")
    read = f.read()
    read.lower()
    wordList = read.split()
    f.close()
    while True:
        letters = raw_input("Enter the letters you have: ").lower()
        baseLetter = raw_input("What letter are you playing off of? ").lower()
        if baseLetter != "none":
            letters += baseLetter
        validWords = []
        twoWords = []
        threWords = []
        fourWords = []
        fiveWords = []
        sixWords = []
        sevnWords = []
        bigWords = []
        for i in wordList:
            valid = 0
            smallList = list(i)
            length = len(smallList)
            if length > 1:
                for j in range(len(letters)):
                    if letters[j] in smallList:
                        index = smallList.index(letters[j])
                        smallList.pop(index)
                        valid += 1
                if valid <= len(letters):
                    if len(smallList) == 0 and baseLetter != "none" and baseLetter != "":
                        validWords.append(i)
                    elif len(smallList) == 0 and baseLetter == "none":
                        validWords.append(i)
                    elif len(smallList) == 1 and baseLetter == "":
                        validWords.append(i)
                    elif len(smallList) == 1 and " " in letters and baseLetter != "none":
                        validWords.append(i)
        for i in validWords:
            if len(i) == 2:
                twoWords.append(i)
            if len(i) == 3:
                threWords.append(i)
            if len(i) == 4:
                fourWords.append(i)
            if len(i) == 5:
                fiveWords.append(i)
            if len(i) == 6:
                sixWords.append(i)
            if len(i) == 7:
                sevnWords.append(i)
            if len(i) > 7:
                bigWords.append(i)
        fullList = bigWords+sevnWords+sixWords+fiveWords+fourWords+threWords+twoWords 
        fullLength = len(fullList)
        option = "Y"
        print "There are",fullLength,"possible words to play."
        while option != "N":
            option = raw_input("How many letter do you want to see? [2-7], greater than 7 [>] or [ALL]: ") or "n"
            option = option.upper()[0]
            if option == "A":
                for i in range(fullLength):
                    print fullList[i]
            if option == "2":
                print len(twoWords),"words."
                for i in twoWords:
                    print i
            if option == "3":
                print len(threWords),"words."
                for i in threWords:
                    print i
            if option == "4":
                print len(fourWords),"words."
                for i in fourWords:
                    print i
            if option == "5":
                print len(fiveWords),"words."
                for i in fiveWords:
                    print i
            if option == "6":
                print len(sixWords),"words."
                for i in sixWords:
                    print i
            if option == "7":
                print len(sevnWords),"words."
                for i in sevnWords:
                    print i
            if option == ">":
                print len(bigWords),"words."
                for i in bigWords:
                    print i

main()
