'''Nigel Hamilton
2/10/15
Roulette v 2.1.0'''

import random as r
import time as t

def single(balance,name,hbal,bet):
    numok1 = 1
    ball = r.randint(1,38)
    while numok1 == 1:
        if name == "Giza":
            ball = r.randint(1,100)
        if name == "59173":
            print "The number is",str(ball)+"."
        guess = raw_input("What number? ")
        if guess.isdigit():
            numok1 = 0
            guess = int(guess)
        else:
            print '"'+guess+'" is an invalid number.'
    if ball == guess:
        t.sleep(3)
        balance = balance+(bet*36)-0.05
        hbal = hbal-(bet*36)+0.05
        print "You win! Your balance is $"+str(balance)+"\n"
    else:
        t.sleep(3)
        balance = balance-bet
        hbal = hbal+bet
        print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    return balance, hbal

def oddeven(balance,hbal,bet):
    choose = raw_input("Do you want to bet (e)ven or (o)dd? ")
    choose = choose.upper()
    ball = r.randint(1,38)
    if choose == "E":
        if ball%2 == 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    if choose == "O":
        if ball%2 != 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    return balance, hbal

def twelves(balance,hbal,bet):
    choose = raw_input("Do you want to bet on the (1)st set of 12, (2)nd set, or (3)rd set? ")
    choose = choose.upper()
    ball = r.randint(1,38)
    if choose == "1":
        if ball < 13:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    if choose == "2":
        if ball < 25 and ball > 12:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    if choose == "3":
        if ball < 37 and ball > 24:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"       
    return balance, hbal

def eighteens(balance,hbal,bet):
    choose = raw_input("Do you want to bet on the (1)st set of 18, or (2)nd set? ")
    choose = choose.upper()
    ball = r.randint(1,38)
    if choose == "1":
        if ball < 19:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    if choose == "2":
        if ball < 37 and ball > 18:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number is",str(ball)+".\n"
    return balance, hbal
    
def color(balance,hbal,bet):
    choose = raw_input("Which color, (r)ed, or (b)lack? ")
    choose = choose.upper()
    ball = r.randint(1,38)
    if choose == "R":
        if ball%2 == 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal =hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number ("+str(ball)+") is black.\n"
    if choose == "B":
        if ball%2 != 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\n\
The correct number ("+str(ball)+") is red.\n"         
    return balance, hbal
