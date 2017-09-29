import random
import time

# Pick random, nonrepeating word from a large list
def pickWord(wordList):
    randomIndex = random.randint(0,len(wordList)-1)
    while letterScore(wordList[randomIndex]) != 5:
        randomIndex = random.randint(0,len(wordList)-1)
    return wordList[randomIndex]

# Give a score to a word to find reapeating letters
def letterScore(word):
    usedLetters = []
    score = 0
    # Score of 1 is 5 letters repeated, 5 is all different, ect.
    for i in word:
        if i not in usedLetters:
            usedLetters.append(i)
            score += 1
    return score

# Open file
def readFile(fileName):
    f = open(fileName, "r")
    return f

# Close file
def closeFile(f):
    f.close()

# Split string of file into a word list
def wordListSplit(wordString):
    return wordString.split()

# Count the number of similar letters between two words
def compareWords(word1, word2):
    word1 = list(word1)
    count = 0
    for i in word1:
        if i in word2:
            count += 1
            word1[:] = (value for value in word1 if value != i)
    return count

# Get a word from user
def userGuess(wordList):
    wordGuess = raw_input("\nEnter a five letter word. ").lower()
    while wordGuess not in wordList or len(wordGuess) != 5:
        print "Sorry, that's not a word."
        wordGuess = raw_input("\nEnter a five letter word. ").lower()
    return wordGuess

# Game
def game(userGuess, wordAnswer):
    wordScore = compareWords(wordAnswer, userGuess)
    print "There is/are " + str(wordScore) + " common letter(s) with my word."

def cleanCheck(letterList, notLetters, knownLetters):
    for i in letterList:
        if i in notLetters or i in knownLetters:
            letterList.remove(i)
    return letterList

def compGuess(wordList, knownLetters, notLetters, checkLetters, prevWords):
    #wordList = scoreWords(wordList, knownLetters, notLetters, checkLetters)
    wordGuess = wordList[random.randint(0, len(wordList)-1)]
    if len(prevWords) > 0:
        if prevWords[-1][1] == 0:
            for i in prevWords[-1][0]:
                notLetters.append(i)
            if len(checkLetters) == 0:
                while compareWords(wordGuess, notLetters) != 0:
                    wordGuess = wordList[random.randint(0, len(wordList)-1)]
            else:
                while compareWords(wordGuess, checkLetters) > 2 or compareWords(wordGuess, notLetters) < 3:
                    wordGuess = wordList[random.randint(0, len(wordList)-1)]
        elif prevWords[-1][1] == 1:
            for i in prevWords[-1][0]:
                if i not in checkLetters and i not in notLetters and i not in knownLetters:
                    checkLetters.append(i)
            checkLetters = cleanCheck(checkLetters, notLetters, knownLetters)
            if compareWords(prevWords[-1][0], knownLetters) == 1:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        notLetters.append(i)
            if compareWords(prevWords[-1][0], notLetters) == 4:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        knownLetters.append(i)
            if len(checkLetters) > 2:
                while compareWords(wordGuess, checkLetters) != 3 or compareWords(wordGuess, notLetters) != 0:
                    wordGuess = wordList[random.randint(0, len(wordList)-1)]
            else:
                if len(knownLetters) < 3:
                    while compareWords(wordGuess, notLetters)+compareWords(wordGuess, knownLetters) > 3:
                        wordGuess = wordList[random.randint(0, len(wordList)-1)]
        elif prevWords[-1][1] == 2:
            for i in prevWords[-1][0]:
                if i not in checkLetters and i not in notLetters and i not in knownLetters:
                    checkLetters.append(i)
            checkLetters = cleanCheck(checkLetters, notLetters, knownLetters)
            if compareWords(prevWords[-1][0], knownLetters) == 2:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        notLetters.append(i)
            if compareWords(prevWords[-1][0], notLetters) == 3:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        knownLetters.append(i)
        elif prevWords[-1][1] == 3:
            for i in prevWords[-1][0]:
                if i not in checkLetters and i not in notLetters and i not in knownLetters:
                    checkLetters.append(i)
            checkLetters = cleanCheck(checkLetters, notLetters, knownLetters)
            if compareWords(prevWords[-1][0], knownLetters) == 3:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        notLetters.append(i)
            if compareWords(prevWords[-1][0], notLetters) == 2:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        knownLetters.append(i)
        elif prevWords[-1][1] == 4:
            for i in prevWords[-1][0]:
                if i not in checkLetters and i not in notLetters and i not in knownLetters:
                    checkLetters.append(i)
            checkLetters = cleanCheck(checkLetters, notLetters, knownLetters)
            if compareWords(prevWords[-1][0], knownLetters) == 4:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        notLetters.append(i)
            if compareWords(prevWords[-1][0], notLetters) == 1:
                for i in prevWords[-1][0]:
                    if i not in knownLetters and i not in notLetters:
                        knownLetters.append(i)
            if compareWords(prevWirds[-1][0], knownLetters) == 4:
                while compareWords(wordGuess, prevWords[-1][0]) != 4 and compareWords(wordGuess, notLetters) != 5:
                    wordGuess = wordList[random.randint(0, len(wordList)-1)]
        elif prevWords[-1][1] == 5:
            for i in prevWords[-1][0]:
                knownLetters.append(i)
            while compareWords(wordGuess, prevWords[-1][0]) != 5:
                wordGuess = wordList[random.randint(0, len(wordList)-1)]
    else:
        while letterScore(wordGuess) != 5:
            wordGuess = wordList[random.randint(0, len(wordList)-1)]
    if len(notLetters) == 0:
        while letterScore(wordGuess) != 5 or compareWords(wordGuess, checkLetters) > 2:
            print compareWords(wordGuess, checkLetters)
            wordGuess = wordList[random.randint(0, len(wordList)-1)]        
    print checkLetters, knownLetters, notLetters
    return wordGuess
    
def scoreWords(wordList, knownLetters, notLetters, checkLetters):
    for i in wordList:
        scoreInfo = letterScore(i)
        for j in i:
            if j in notLetters:
                scoreInfo += 2
            if j in knownLetters:
                scoreInfo -= 1
            if j in checkLetters:
                scoreInfo += 4
        if scoreInfo == letterScore(i):
            scoreInfo += 10
        tpl = (i,scoreInfo)
        wordList.insert(wordList.index(i), tpl)
        wordList.pop(wordList.index(i))
    return wordList

# Main
def main():
    f = readFile("C:/Users/Nigel/Documents/My Programs/Python/Jotto/fiveWordList.txt")
    wordString = f.read()
    closeFile(f)
    wordList = wordListSplit(wordString)
    wordAnswer = pickWord(wordList)
    wordGuess = ""
    knownLetters = []
    notLetters = []
    checkLetters = []
    prevWords = []
    guesses = 0
    while wordGuess != wordAnswer:
        #wordGuess = userGuess(wordList)
        #game(wordGuess, wordAnswer)
        guesses += 1
        guess = compGuess(wordList, knownLetters, notLetters, checkLetters, prevWords)
        print guess
        score = input("")
        prevWords.append((guess, score))
        print prevWords
    print "You got it in " + str(guesses) + " guesses!"

#main()
    
    
    
