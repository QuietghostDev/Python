'''Quotes
Nigel Hamilton
5/7/15'''

from random import *
from time import *

def main():
    fl = open("quotes","r")
    flLst = fl.readlines()
    fl.close()
    turns = 0
    score = 0
    combo = 1 #Combo rises as you get more right in a row
    letters = ["a","b","c","d","e"] #This makes the multiple choice better
    usedQuotes = []
    name = raw_input("What's your name? ")
    start = round(time(),1) #Start
    while (turns <= 9):
        authors = []
        index = randint(0,4)
        quote = flLst[randint(0,len(flLst)-1)]
        while (quote in usedQuotes):
            quote = flLst[randint(0,len(flLst)-1)]
        print
        print quote[:(quote.index("%"))],"\n"
        for i in range(4):
            quoteFake = flLst[randint(0,len(flLst)-1)]
            while (quoteFake[(quoteFake.index("%"))+1:] == quote[(quote.index("%"))+1:]) | (quoteFake[(quoteFake.index("%"))+1:] in authors):
                #Makes sure that the options don't repeat
                quoteFake = flLst[randint(0,len(flLst)-1)]
            authors.append(quoteFake[(quoteFake.index("%"))+1:])
        authors.insert(index,quote[(quote.index("%"))+1:])
        for i in range(5):
            print letters[i]+".",authors[i].strip()
        print
        ans = raw_input("Who said it? ")
        if (ans == letters[index]):
            print "You are right!"
            score += combo*1000
            combo += 1
        else:
            print "Incorrect,",authors[index].strip(),"said this."
            combo = 1
        usedQuotes.append(quote)
        turns += 1
    end = round(time(),1)
    score -= int(10*(end-start))
    print "Thats the game, folks."
    print "Score:",score
    flScr = open("scores","r")
    flScrRd = flScr.readlines()
    for i in flScrRd:
        flScrRd[flScrRd.index(i)] = (i[:i.index("%")],eval(i[i.index("%")+1:]))
    tpl = (name,score)
    flScrRd.append(tpl)
    flScrRd.sort(key = lambda score: score[1],reverse = True)
    count = 0
    print "\nHighscores:\n"
    while (count < 10 and count < len(flScrRd)):
        print str(count+1)+".",flScrRd[count][0]+":",flScrRd[count][1]
        count += 1
    flScr.close()
    flScr = open("scores","w")
    for i in flScrRd:
        flScr.write(i[0]+"%"+str(i[1])+"\n")

main()
