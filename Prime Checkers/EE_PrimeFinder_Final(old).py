import math
# Eli Eisenstein
# 11/14/14
# This program determines if an input is prime.

import time
restart = "Y"
print "This program will determine weather the number you input is prime. \n Any large number may take a very long time."
def primefinder():
    divisor = 2
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
        while divisor != testnumber:

            if inputnumber % divisor != 0:
                divisor = divisor + 1

            else:
                print inputnumber, 'is not prime.'
                print 'Factor is:', divisor
                prime = 0
                divisor = testnumber
                timer2 = time.time()
                timer3 = timer2 - timer1
                print "Time elapsed:", round(timer3, 4), 'seconds.'

        if (prime == 1) and (inputnumber !=2):
            print inputnumber, 'is prime.'
            timer2 = time.time()
            timer3 = timer2 - timer1
            print "Time elapsed:", round(timer3, 4), 'seconds.'

while restart == "Y":
    primefinder()
    restart = raw_input("\nWould you like to restart? (Y / N): ")
    restart = restart.upper()
