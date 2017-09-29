#Sun calculator, Nigel Hamilton

from math import *

def main():
    valid = 0
    while valid == 0:
        dayYear = raw_input("Enter day as days after new years. ")
        try:
            float(dayYear)
            valid = 1
        except:
            ValueError
    dayYear = eval(dayYear)
    print dayYear
    sunRise = 416+84*cos(3.1415/182(dayYear-356))
    sunSet = 1117.5+115.5*cos(3.1415/182(dayYear-172))
    dayTime = 720+180.6666*cos(3.1415/182(dayYear-172))
    print "On the",dayYear,"day of the year the sun rises at",sunRise,"minutes after midnight."
    print "The sun sets at",sunSet,"minutes after midnight."
    print "The day is",dayTime,"minutes long."

main()
