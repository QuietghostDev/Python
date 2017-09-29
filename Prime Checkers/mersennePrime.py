import math
import time

def lucasLehmer(power,num):
    sequenceNum = 4
    position = 1
    tAve = time.time()
    while position < power-1:
        sequenceNum = pow(sequenceNum,2,num)-2
        position += 1
        if position%1000 == 0:
            tEst = round(((time.time()-tAve)/1000)*(power-position),3)
            tFin = time.time()+tEst
            tEstH = int(tEst)/3600
            tEst -= tEstH*3600
            tEstM = int(tEst)/60
            tEst -= tEstM*60
            tEstS = tEst
            tAve = time.time()
            percent = round((position/(power-1.0))*100,2)
            print "Update: "+time.ctime()
            print "\tIteration: "+str(position)+", "+str(percent)+"%"
            print "\tEstimated time:",tEstH,"hour(s),",tEstM,"minute(s), and",tEstS,"second(s)."
            print "\tEstimated Finish: "+time.ctime(tFin)+".\n"
    return sequenceNum

def primality(power):
    t1 = time.time()
    num = (2**power)-1
    print "\nStart: M"+str(power)+", "+time.ctime()+"\n"
    multiple = lucasLehmer(power,num)
    print "Finish: "+time.ctime()+"\n"
    t2 = round(time.time()-t1,3)
    th = int(t2)/3600
    t2 -= th*3600
    tm = int(t2)/60
    t2 -= tm*60
    ts = t2
    if multiple%num == 0:
        print th,"hour(s),",tm,"minute(s), and",ts,"second(s)."
        print "M"+str(power)+" is prime!\n"
        return True
    else:
        print th,"hour(s),",tm,"minute(s), and",ts,"second(s)."
        print "M"+str(power)+" is composite.\n"
        return False

def main():
    power = input("Enter a power to be tested: ")
    primality(power)

main()
