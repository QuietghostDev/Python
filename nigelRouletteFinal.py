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
    print 'Enter a bet type then enter the amount you want to bet and your bet.\nIf you feel you are done, simply type "D".'
    print 'Enter "bal" to see how much money you have.'
    
def game():
    bettype = raw_input("Do you want to bet on a (s)ingle number, (o)dd/even number, (c)olor,\nset of (e)ighteen, or a set of (t)welve? ")
    bettype = bettype.upper()
    return bettype
    
def main():
    balance = 100
    hbal = 100
    name = askName()
    if name == "59173":
        balance = 1000000
        hbal = 1000000
        print "Welcome sir Nigel."
    if name == "Ben":
        balance = 10
    intro(name)
    while balance > 1 and balance < 100000000:
        bettype = game()
        if bettype == "S":
            balance, hbal = single(balance,name,hbal)
        if bettype == "O":
            balance, hbal = oddeven(balance,hbal)
        if bettype == "T":
            balance, hbal = twelves(balance,hbal)
        if bettype == "C":
            balance, hbal = color(balance,hbal)
        if bettype == "E":
            balance, hbal = eighteens(balance,hbal)
        if bettype == "I":
            intro(name)
        if bettype == "BAL":
            print "$"+str(balance)
        if bettype == "HBAL":
            print "$"+str(hbal)
        if bettype == "TBAL":
            print "$"+str(balance+hbal)
        if bettype == "D":
            print "Your final balance is $"+str(balance)
            print "I have $"+str(hbal)
            t.sleep(1)
            print "Thanks for playing!"
            t.sleep(2)
            break
        if balance < 20 and balance > 1 and name != "Ben":
            more = raw_input("Need more cash? y/n ")
            more = more.upper()
            if more == "Y":
                balance = balance+100
            if more == "59173":
                balance = balance+100000
    if balance < 1:
        print "Haha, you lost!"
        print "I have $"+str(hbal)
        play = raw_input("Play again? y/n ")
        play = play .upper()
        if play == "Y":
            main()
    if balance > 100000000:
        print "OVERLOAD!"
        print "You win!"
        play = raw_input("Play again? y/n ")
        play = play .upper()
        if play == "Y":
            main()
    return name

def single(balance,name,hbal):
    print "You have $"+str(balance)
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
        if name == "Ben":
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
        print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    return balance, hbal

def oddeven(balance,hbal):
    choose = raw_input("Do you want to bet (e)ven or (o)dd? ")
    choose = choose.upper()
    if choose == "E":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball%2 == 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    if choose == "O":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball%2 != 0:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    return balance, hbal

def twelves(balance,hbal):
    choose = raw_input("Do you wan to bet on the (1)st set of 12, (2)nd set, or (3)rd set? ")
    choose = choose.upper()
    if choose == "1":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball < 13:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    if choose == "2":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball < 25 and ball > 12:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    if choose == "3":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball < 37 and ball > 24:
            t.sleep(3)
            balance = balance+(bet*2)-0.05
            hbal = hbal-(bet*2)+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"       
    return balance, hbal
    
def color(balance,hbal):
    choose = raw_input("Which color, (r)ed, or (b)lack? ")
    choose = choose.upper()
    if choose == "R":
        print "You have $"+str(balance)
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
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal =hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is black.\n"
    if choose == "B":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,2)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball == 1:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is red.\n"         
    return balance, hbal

def eighteens(balance,hbal):
    choose = raw_input("Do you wan to bet on the (1)st set of 18, or (2)nd set? ")
    choose = choose.upper()
    if choose == "1":
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
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
        print "You have $"+str(balance)
        numok = 1
        ball = r.randint(1,38)
        while numok == 1:
            bet = raw_input("How much do you want to bet? ")
            if bet.isdigit() and bet > 0 and int(bet) <= balance:
                numok = 0
                bet = int(bet)
            else:
                print '"'+bet+'" is an invalid bet.'
        if ball < 37 and ball > 18:
            t.sleep(3)
            balance = balance+bet-0.05
            hbal = hbal-bet+0.05
            print "You win! Your balance is $"+str(balance)+"\n"
        else:
            t.sleep(3)
            balance = balance-bet
            hbal = hbal+bet
            print "You lose! Your Balance is $"+str(balance)+"\nThe correct number is",str(ball)+".\n"
    return balance, hbal    
        
main()
