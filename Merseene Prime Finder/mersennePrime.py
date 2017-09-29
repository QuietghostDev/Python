import math
import time

def lucasLehmer(power,num):
    sequenceNum = 4
    position = 1
    tAve = time.time()
    for i in range(2,power):
        sqr = sequenceNum*sequenceNum
        sequenceNum = (sqr&num)+(sqr>>power)
        if sequenceNum >= num:
            sequenceNum -= num
        sequenceNum -= 2
        if i%1000 == 0:
            tEst = round(((time.time()-tAve)/1000)*(power-i),3)
            tFin = time.time()+tEst
            tEstH = int(tEst)/3600
            tEst -= tEstH*3600
            tEstM = int(tEst)/60
            tEst -= tEstM*60
            tEstS = tEst
            tAve = time.time()
            percent = round((i/(power-1.0))*100,2)
            print "Update: "+time.ctime()
            print "\tIteration: "+str(i)+", "+str(percent)+"%"
            print "\tEstimated time:",tEstH,"hour(s),",tEstM,"minute(s), and",tEstS,"second(s)."
            print "\tEstimated Finish: "+time.ctime(tFin)+".\n"
    return sequenceNum

def primality(power):
    timeStart = time.time()
    num = (2<<(power-1))-1
    length = int(math.ceil(power/3.321928094887363))
    print "\nStart: M"+str(power)+", "+time.ctime()
    print "Length: "+str(length)+"\n"
    multiple = lucasLehmer(power,num)
    print "Finish: "+time.ctime()+"\n"
    timeEnd = round(time.time()-timeStart,3)
    timeHour = int(timeEnd)/3600
    timeEnd -= timeHour*3600
    timeMinute = int(timeEnd)/60
    timeEnd -= timeMinute*60
    timeSecond = timeEnd
    if multiple%num == 0:
        print timeHour,"hour(s),",timeMinute,"minute(s), and",timeSecond,"second(s)."
        print "M"+str(power)+" is prime!\n"
        return True
    else:
        print timeHour,"hour(s),",timeMinute,"minute(s), and",timeSecond,"second(s)."
        print "M"+str(power)+" is composite.\n"
        return False
