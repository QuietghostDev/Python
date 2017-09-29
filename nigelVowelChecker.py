'''Nigel
Vowel checker
3/4/15'''

from time import *

def tryopen(f):
    try:
        x = open(f, "r")
        return True
    except IOError:
        return False

def vowels():
    do = "Y"
    valid = 0
    while do == "Y":
        vowelsA = 0
        vowelsE = 0
        vowelsI = 0
        vowelsO = 0
        vowelsU = 0
        while valid == 0:
            f = raw_input("Enter a file name: ")
            if tryopen(f):
                valid = 1
            else:
                print "I could not find that file."
        valid = 0
        x = open(f, "r")
        string = x.read().upper()
        timeS = time()
        print "That file has,",len(string),"characters."
        for i in range(len(string)):
            if string[i] == "A":
                vowelsA += 1
            elif string[i] == "E":
                vowelsE += 1
            elif string[i] == "I":
                vowelsI += 1
            elif string[i] == "O":
                vowelsO += 1
            elif string[i] == "U":
                vowelsU += 1
        timeE = time()
        timeElapse = timeE-timeS
        print "There are,",vowelsA,"A's,",vowelsE,"E's",vowelsI,"I's",vowelsO,"O's, and",vowelsU,"U's."
        print "That took",round(timeElapse, 3),"seconds."
        do = raw_input("See another file? ").upper()[0]

def punctuation():
    do = "Y"
    valid = 0
    while do == "Y":
        puncte = 0
        punctq = 0
        punctp = 0
        punctc = 0
        puncts = 0
        punctcl = 0
        while valid == 0:
            f = raw_input("Enter a file name: ")
            if tryopen(f):
                valid = 1
            else:
                print "I could not find that file."
        valid = 0
        x = open(f, "r")
        string = x.read().upper()
        timeS = time()
        print "That file has,",len(string),"characters."
        for i in range(len(string)):
            if string[i] == "!":
                puncte += 1
            elif string[i] == "?":
                punctq += 1
            elif string[i] == ".":
                punctp += 1
            elif string[i] == ",":
                punctc += 1
            elif string[i] == ";":
                puncts += 1
            elif string[i] == ":":
                punctcl += 1
        timeE = time()
        timeElapse = timeE-timeS
        print "There are,",punctp,"periods,",punctc,"commas,",punctq,"question marks,",puncte,"exclamation marks,",puncts,"semi-colons and,",punctcl,"colons."
        print "That took",round(timeElapse, 3),"seconds."
        do = raw_input("See another file? ").upper()[0]


