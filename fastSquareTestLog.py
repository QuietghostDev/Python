import time
import math
import random

def main():
    for i in range(10):
        power = 10000000
        offset = 100000000000000000000000000000000000000000000000
        num = (2<<(power-1))-offset
        timeShift = time.time()
        #power = len(bin(num))-2#int(math.ceil(math.log(num,2)))
        #offset = (2<<(power-1))-num
        numSq = (num+offset<<power)-((num+offset)*(2*offset)-offset**2)
        timeShiftE = time.time()-timeShift
        print "\n\tDone Shift Square",round(timeShiftE,4),"seconds."
        timeNorm = time.time()
        numSq2 = pow(num,2)
        timeNormE = time.time()-timeNorm
        print "\tDone Normal Square",round(timeNormE,4),"seconds."
        if timeShiftE < timeNormE:
            print "Shift is faster by,",round(timeNormE-timeShiftE,4),"seconds."
        else:
            print "Normal is faster by,",round(timeShiftE-timeNormE,4),"seconds."

main()
