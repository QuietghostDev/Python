#11/14/14
#Nigel Hamilton, Eli Eisenstein
#Prime Number Checker, Final Edition
import time

play = "Y"
print "This is a prime number checker, it will tell if the number you put in, is prime or not"
def primeCheck():
    isprime = 1
    div = 3
    while isprime == 1:
        numini = input("Enter a number:\n")
        numinf = numini**0.5
        start = time.time()
        if numini%2 == 0:
            print numini,"is not prime."
            print "The lowest factor is 2"
            isprime = 0
            end = time.time()
            elapse = end-start
            print "That took",round(elapse, 4),"seconds."
        else:        
            while div < numinf:
                if numini%div != 0:
                    div = div+2
                else:
                    print numini,"is not prime."
                    print "The lowest factor is",div
                    end = time.time()
                    elapse = end-start
                    print "That took",round(elapse, 4),"seconds"
                    isprime = 0
            if div > numinf:
                print numini,"is prime!"
                end = time.time()
                elapse = end-start
                print "That took",round(elapse, 4),"seconds."
                isprime = 0
primeCheck()
