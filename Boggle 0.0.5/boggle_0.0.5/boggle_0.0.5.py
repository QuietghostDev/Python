'''Nigel
10/21/15
Boggle v. 0.0.4'''

#TODO Fix multi-letter problem

from random import *
import findWord

#Gloabal Variables
seq = [""]
neighbors = []

#Build borad of random letters
def buildBoard():
    board = [['']*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = chr(randint(65,90))
    return board

#Replace used letters
def fixBoard(seq,board,pos,posBoard):
    row,col = findLetter(seq,board,pos,posBoard)
    board[row].pop(col)
    board[row].insert(col,0)
    return board

#Compare the sequence to guess
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

#Find letter in board
def findLetter(seq,board,pos,posBoard):
    row = []
    col = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == seq[pos]:
                row.append(i)
                col.append(j)
    return row[posBoard],col[posBoard]

#Find neighbors given a letter
def neighbors(seq,board,pos,posBoard):
    neighbors = [] #Blank list
    row,col = findLetter(seq,board,pos,posBoard) #Position of letter on board
    for i in range(-1,2):
        for j in range(-1,2):
            if row+i >= 0 and row+i <=3 and col+j >= 0 and col+j <= 3: #Fixes edge cases
                if board[row+i][col+j] != seq[pos]:
                    neighbors.append(board[row+i][col+j]) #All letters in 3x3 grid around letter put in list
    return neighbors

#Show generated board
def showBoard(boardDummy):
    for i in range(4):
        print boardDummy[i]

#User interface
def userInput():
    guess = raw_input("Enter a word: ").upper()
    return guess

#Build seq based on neighbors
def sequence(guess,board):
    seq = [guess[0]] #Seq-Sequence set to first letter of guess
    count = 0 #Index of neighbors
    pos = 0 #Index of seq
    posBoard = 0 #Index of letter list on board
    found = 0 #If found, 1, if not, -1, else, 0
    boardDummy = board
    while compareWord(guess,seq) != 1 and found == 0:
        while compareWord(guess,seq) == -1 and found == 0:
            print seq,neighbors(seq,board,pos,posBoard)
            if count == len(neighbors(seq,board,pos,posBoard)):
                print "Not found"
                posBoard += 1
                count = 0
                board = boardDummy
            seq.insert(len(seq),neighbors(seq,board,pos,posBoard)[count])
            seq.pop(len(seq)-2)
            count += 1
            if compareWord(guess,seq) == 0:
                board = fixBoard(seq,board,pos,posBoard)
                pos += 1
        while compareWord(guess,seq) == 0:
            count = 0
            posBoard = 0
            print seq,neighbors(seq,board,pos,posBoard)
            seq.insert(len(seq),neighbors(seq,board,pos,posBoard)[count])
            if compareWord(guess,seq) != -1:
                board = fixBoard(seq,board,pos,posBoard)
                pos += 1
            elif compareWord(guess,seq) == -1:
                break
    if compareWord(guess,seq) == 1:
        print "Found"
        word = ""
        for i in seq:
            word += i
        word = word.lower()
        if findWord.findWord(word):
            print "In dictionary"
        

#Run it all
def main():
    board = buildBoard()
    showBoard(board)
    guess = userInput()
    sequence(guess,board)
