'''Nigel
10/21/15
Boggle'''

from random import *

seq = [""]
neighbors = []

def buildBoard(): #TODO Fix repeat letter problem
    board = [['']*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = chr(randint(65,90))
    #board = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P']]
    boardDummy = board
    return board,boardDummy

def fixBoard(seq,board,pos):
    row,col = findLetter(seq,board,pos)
    board[row].pop(col)
    board[row].insert(col,0)
    return board

def readFile():
    pass

def checkWord(guess):
    for i in range(4):
        for j in range(4):
            pass
    

def compareWord(guess,seq):
    i = 0
    while i < len(seq):
        if seq[i] != guess[i]:
            return -1
        i += 1
    if len(seq) == len(guess):
        return 1
    elif len(seq) > len(guess):
        raise Exception("sequence longer than guess")
    else:
        return 0

def findLetter(seq,board,pos):
    for i in range(4):
        for j in range(4):
            if board[i][j] == seq[pos]:
                row = i
                col = j
                return row,col
    raise Exception("First letter not found")

def neighbors(seq,board,pos):
    neighbors = []
    row,col = findLetter(seq,board,pos)
    for i in range(-1,2):
        for j in range(-1,2):
            if row+i >= 0 and row+i <=3 and col+j >= 0 and col+j <= 3:
                if board[row+i][col+j] != seq[pos]:
                    neighbors.append(board[row+i][col+j])
    return neighbors

def showBoard():
    boardDummy = buildBoard()[1]
    for i in range(4):
        print boardDummy[i]

def userInput():
    guess = raw_input("Enter a word: ").upper()
    return guess

def sequence(guess):
    seq = [guess[0]]
    count = 0
    pos = 0
    board = buildBoard()[0]
    found = 0
    while compareWord(guess,seq) != 1 and found == 0:
        while compareWord(guess,seq) == -1 and found == 0:
            seq.insert(len(seq),neighbors(seq,board,pos)[count])
            seq.pop(len(seq)-2)
            count += 1
            if count == len(neighbors(seq,board,pos)):
                print "Not found"
                found = -1
            if compareWord(guess,seq) == 0:
                board = fixBoard(seq,board,pos)
                pos += 1
        while compareWord(guess,seq) == 0:
            count = 0
            seq.insert(len(seq),neighbors(seq,board,pos)[count])
            if compareWord(guess,seq) != -1:
                board = fixBoard(seq,board,pos)
                pos += 1
            elif compareWord(guess,seq) == -1:
                break
    if compareWord(guess,seq) == 1:
        print "Found"
    #return seq,neighbors,pos

def main():
    board = buildBoard()
    showBoard()
    guess = userInput()
    sequence(guess)
    #print checkWord(guess)

main()