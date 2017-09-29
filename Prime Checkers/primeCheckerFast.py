#11/13/14, Nigel, Prime Checker
import time
def prime():
    play = "Y"
    print "This is a program that will tell whether a number is prime or not."
    time.sleep(1)
    if play == "TREE":
        print "Nope"
        play = raw_input("Test another number? y/n\n")
        play = play.upper()
    while play == "Y":
        numin = input("Enter a number:\n")
        numinf = numin**0.5
        start = time.time()
        isprime = 1
        div = 3
        if numin%2 == 0 and numin != 2:
            print numin,"is not prime."
            print "The lowest factor is 2"
            isprime = 0
            end = time.time()
            elapse = end-start
            print "That took",round(elapse, 4),"seconds."
            play = raw_input("Test another number? y/n\n")
            play = play.upper()
        if numin == 2:
            print numin,"is prime."
            isprime = 0
            end = time.time()
            elapse = end-start
            print "That took",round(elapse, 4),"seconds."
            play = raw_input("Test another number? y/n\n")
            play = play.upper()
        while isprime:
            numout = numin%div
            if numout == 0 and numin != 2:
                print numin,"is not prime."
                print "The lowest factor is",div
                isprime = 0
                end = time.time()
                elapse = end-start
                if elapse > 60:
                    mins = int(elapse/60)
                    print "That took",mins,"minutes and",round(elapse%60, 4),"seconds."
                else:
                    print "That took",round(elapse, 4),"seconds."
                play = raw_input("Test another number? y/n\n")
                play = play.upper()
            else:
                div = 2+div
            if div > numinf:
                print numin,"is prime!"
                isprime = 0
                end = time.time()
                elapse = end-start
                if elapse > 60:
                    mins = int(elapse/60)
                    print "That took",mins,"minutes and",round(elapse%60, 4),"seconds."
                else:
                    print "That took",round(elapse, 4),"seconds."
                play = raw_input("Test another number? y/n\n")
                play = play.upper()                   
prime()
