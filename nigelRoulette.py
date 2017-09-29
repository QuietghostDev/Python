#Nigel Hamilton
#12/11/14
#Roulette

import random as r
import time as t

def askName():
    name = raw_input("What is your name?\nName: ")
    return name

def intro(name):
    print "Welcome to my roulette",name+"!"
    t.sleep(2)
    print 'Enter a bet type then enter the amount you want to bet and your bet.\nIf you feel you are done, simple type "D".'
def game():
    t.sleep(2)
    bettype = raw_input("Do you want to bet on a (s)ingle number or(o)dd/even number? ")
    bettype = bettype.upper()
    return bettype
    
def main():
    balance = 100
    name = askName()
    if name == "Nigel":
        balance = 1000000
        print "Welcome sir",name+"."
    if name == "Giza":
        balance = 10
    intro(name)
    while balance > 0:
        bettype = game()
        if bettype == "S":
            balance = single(balance,name)
        if bettype == "O":
            balance = oddeven(balance)
        if bettype == "D":
            print "Your final balance is $"+str(balance)+"."
            t.sleep(1)
            print "Thanks for playing!"
            t.sleep(2)
            break
    if balance == 0:
        print "Haha, you lost!"
        play = raw_input("Play again? y/n ")
        play = play .upper()
        if play == "Y":
            main()
    return name
def single(balance,name):
    print "You have $"+str(balance)+"."
    numok = 1
    numok1 = 1
    ball = r.randint(1,38)
    while numok == 1:
        bet = raw_input("How much do you want to bet? ")
        if bet.isdigit() and bet > 0 and int(bet) <= balance:
            numok = 0
            bet = int(bet)
        else:
            print '"'+bet+'" is an invalid bet.'
    while numok1 == 1:
        if name == "Giza":
            ball = r.randint(1,100)
        guess = raw_input("What number? ")
        if guess.isdigit():
            numok1 = 0
            guess = int(guess)
        else:
            print '"'+guess+'" is an invalid number.'
    if ball == guess:
        t.sleep(3)
        balance = balance+(bet*36)
        print "You win! Your balance is $"+str(balance)+".\n"
    else:
        t.sleep(3)
        balance = balance-bet
        print "You lose! Your Balance is $"+str(balance)+".\nThe correct number is",str(ball)+".\n"
    return balance

def oddeven(balance):
    choose = raw_input("Do you want to bet (e)ven or (o)dd? ")
    choose = choose.upper()
    if choose == "E":
        print "You have $"+str(balance)+"."
        numok = 1
        ball = r.randint(1,2)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball == 2:
            t.sleep(3)
            balance = balance+(bet*2)
            print "You win! Your balance is $"+str(balance)+".\n"
        else:
            t.sleep(3)
            balance = balance-bet
            print "You lose! Your Balance is $"+str(balance)+".\nThe correct number is odd.\n"
    if choose == "O":
        print "You have $"+str(balance)+"."
        numok = 1
        ball = r.randint(1,2)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print bet,"is an invalid bet."
        if ball == 1:
            t.sleep(3)
            balance = balance+(bet*2)
            print "You win! Your balance is $"+str(balance)+".\n"
        else:
            t.sleep(3)
            balance = balance-bet
            print "You lose! Your Balance is $"+str(balance)+".\nThe correct number is even.\n"
    return balance

main()
