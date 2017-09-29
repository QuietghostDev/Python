'''Nigel Hamilton
11/5/15
Find word in dictionary'''

import os

def readFile():
    path = os.getcwd()
    fl = open(path+"/finalWordList.txt","r")
    readFl = fl.read()
    wordList = readFl.split()
    fl.close()
    return wordList

def findWord(word):
    wordList = readFile()
    if word in wordList:
        return True
    else:
        return False
