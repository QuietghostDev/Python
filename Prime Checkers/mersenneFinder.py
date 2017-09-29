import mersennePrime
import FermatPrimality
import time

def main():
    currentPrime = 8001
    limit = 9000
    primes = []
    while currentPrime < limit:
        if quickPrimes(2**currentPrime-1):
            if mersennePrime.primality(currentPrime):
                primes.append("M"+str(currentPrime))
                time.sleep(10)
            currentPrime += 2
        else:
            print "M"+str(currentPrime)+" is composite.\n"
            currentPrime += 2
        while not FermatPrimality.fermat(currentPrime):
            currentPrime += 2
        print primes

def quickPrimes(numTest):
    div = 3
    if (numTest%2 == 0):
        return False
    while (div <= 100000):
        if (numTest%div == 0):
            return False
        else:
            div += 2
    return True

main()
