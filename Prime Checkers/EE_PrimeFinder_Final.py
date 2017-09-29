import math
# Eli Eisenstein
# 11/14/14
# This program determines if an input is prime.

import time
restart = "Y"
print "This program will determine weather the number you input is prime. \n Any large number may take a very long time."
def primefinder():
    divisor = 3
    prime = 1
    inputnumber = input("Enter a number: ")
    testnumber = int( math.sqrt(inputnumber))
    timer1 = time.time()

    if inputnumber == 2:
        print "2 is the only even prime number."
        timer2 = time.time()
        timer3 = timer2 - timer1
        print "Time elapsed:", round(timer3), 'seconds.'

    else:
        if inputnumber%2 == 0:
                print inputnumber, 'is not prime.'
                print 'Factor is: 2'
                prime = 0
                divisor = testnumber
                timer2 = time.time()
                timer3 = timer2 - timer1
                print "Time elapsed:", round(timer3), 'seconds.'
        while divisor != testnumber:

            if inputnumber % divisor != 0:
                divisor = divisor + 2

            else:
                print inputnumber, 'is not prime.'
                print 'Factor is:', divisor
                prime = 0
                divisor = testnumber
                timer2 = time.time()
                timer3 = timer2 - timer1
                print "Time elapsed:", round(timer3), 'seconds.'

        if (prime == 1) and (inputnumber !=2):
            print inputnumber, 'is prime.'
            timer2 = time.time()
            timer3 = timer2 - timer1
            print "Time elapsed:", round(timer3, 5), 'seconds.'

while restart == "Y":
    primefinder()
    restart = raw_input("\nWould you like to restart? (Y / N): ")
    restart = restart.upper()
