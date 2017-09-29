import mersennePrime
import FermatPrimality
import time

def main():
    currentPrime = 19501
    limit = 20000
    primes = []
    while currentPrime < limit:
        if mersennePrime.primality(currentPrime):
            primes.append("M"+str(currentPrime))
            time.sleep(10)
        currentPrime += 2
        while not FermatPrimality.fermat(currentPrime):
            currentPrime += 2
    print primes

main()
