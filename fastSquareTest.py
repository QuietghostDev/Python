import time

def main():
    power = input("Enter power ")
    offset = input("Enter offset ")
    num = 2**power-offset
    timeShift = time.time()
    numSq = (num+offset<<power)-((num+offset)*(2*offset)-offset**2)
    timeShiftE = time.time()-timeShift
    print "\tDone Shift Square",round(timeShiftE,4),"seconds."
    timeNorm = time.time()
    numSq2 = pow(num,2)
    timeNormE = time.time()-timeNorm
    print "\tDone Normal Square",round(timeNormE,4),"seconds.\n"
    if timeShiftE < timeNormE:
        print "Shift is faster by,",round(timeNormE-timeShiftE,4),"seconds."
    else:
        print "Normal is faster by,",round(timeShiftE-timeNormE,4),"seconds."

main()
