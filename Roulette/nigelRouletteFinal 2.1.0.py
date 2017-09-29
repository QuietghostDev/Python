'''Nigel Hamilton
2/10/15
Roulette v 2.1.0'''

import time as t
from nigelRouletteFinalGametypes import *


def askName():
    name = raw_input("What is your name?\nName: ")
    return name

def intro(name):
    print "Welcome to my roulette",name+"!"
    t.sleep(2)
    print 'Enter a bet type then enter the amount you want to bet and your bet.\nIf you feel you are done, simply type "D".'
    print 'Enter "bal" to see how much money you have.'

def isFloat(bet):
    try:
        float(bet)
        return True
    except ValueError:
        return False

def numberOk(bet):
    bet = int(bet*100)
    bet = bet/100.00
    return bet
    
def game():
    bettype = raw_input("Do you want to bet on a (s)ingle number, (o)dd/even number, (c)olor,\nset of (e)ighteen or a set of (t)welve? ")
    bettype = bettype.upper()
    return bettype

def userBet(balance):
    print "You have $"+str(balance)
    numok = 1
    while numok == 1:
        bet = raw_input("How much do you want to bet? $")
        if isFloat(bet) and eval(bet) >= 0.01 and eval(bet) <= balance:
            numok = 0
            bet = eval(bet)
            bet = numberOk(bet)
        else:
            print '"'+bet+'" is an invalid bet.'
    return bet, balance
    
def main():
    balance = 100
    hbal = 100
    owed = 0
    more = "FILLER"
    name = askName()
    if name == "59173":
        balance = 1000000
        hbal = 1000000
        print "Welcome sir Nigel."
    if name == "Giza":
        balance = 10
        more = "NO"
    intro(name)
    while balance > 0:
        bettype = game()
        if bettype == "S":
            bet, balance = userBet(balance)
            balance, hbal = single(balance,name,hbal,bet)
        if bettype == "O":
            bet, balance = userBet(balance)
            balance, hbal = oddeven(balance,hbal,bet)
        if bettype == "T":
            bet, balance = userBet(balance)
            balance, hbal = twelves(balance,hbal,bet)
        if bettype == "E":
            bet, balance = userBet(balance)
            balance, hbal = eighteens(balance,hbal,bet)
        if bettype == "C":
            bet, balance = userBet(balance)
            balance, hbal = color(balance,hbal,bet)
        if bettype == "I":
            intro(name)
        if bettype == "BAL":
            print "$"+str(balance)
            more = "FILLER"
        if bettype == "HBAL":
            print "$"+str(hbal)
        if bettype == "RESET":
            main()
        if bettype == "D":
            print "You owe: $"+str(owed)
            owed += owed*0.02
            owed = numberOk(owed)
            print "Total bill with 2% intrest: $"+str(owed)
            balance = balance-owed
            hbal = hbal+owed
            print "Your final balance is $"+str(balance)
            if hbal < 100:
                print "The house lost $"+str((hbal-100)*-1)
            else:
                print "The house gained $"+str(hbal-100)
            t.sleep(1)
            print "Thanks for playing!"
            t.sleep(2)
            break
        if balance < 20 and balance >= 0.01 and more != "NO" or bettype == "MORE":
            more = raw_input("Need more cash? y/n ")
            more = more.upper()
            numok = 1
            if more == "Y":
                while numok == 1:
                    add = raw_input("How much? $")
                    if isFloat(add) and eval(add) >= 0.01 and eval(add) < 10000:
                        numok = 0
                        add = eval(add)
                        add = numberOk(add)
                        balance = balance+add
                        owed = owed+add
                        print "Ok, you now owe: $"+str(owed)
                    else:
                        print '"'+add+'" is an invalid amount.'
            if more == "59173":
                balance = balance+100000
                owed = owed+100000
        if bettype == "PAY":
            if owed == 0:
                print "You owe nothing."
            else:
                print "You owe: $"+str(owed)
                print "Your balance: $"+str(balance)
                veri = raw_input("Are you sure you want to continue? y/n ")
                veri = veri.upper()
                if veri == "Y" and balance-(owed+owed*0.02) > 0:
                    balance = balance-(owed+owed*0.02)
                    hbal = hbal+(owed+owed*0.02)
                    hbal = numberOk(hbal)
                    balance = numberOk(balance)
                    owed = 0
                    print "You now have $"+str(balance)
                elif balance-(owed+owed*0.02) < 0:
                    print "You do not have the money to pay that off."
    if balance == 0 and bettype != "D":
        print "Haha, you lost!"
        print "I have $"+str(hbal)
        play = raw_input("Play again? y/n ")
        play = play .upper()
        if play == "Y":
            main()
    return name
        
main()
