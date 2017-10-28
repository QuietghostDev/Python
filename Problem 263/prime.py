from random import randint


# This is for raising numbers to extraordinary powers, but having a modulus
# it returns m^e (mod n), or in python (m**e)%n.
# But you cannot raise 20^234987987234 first, it would overflow, so this gives you a way to do that
def modpower(m, e, n, debug=False):
    a = []
    if (debug):
        print('squaring down')
    while (e > 0):
        if (e % 2 == 1):
            a.append(m)
            e = e - 1
        m = m * m % n
        e = e / 2
    if (debug):
        print('multiplying up')
    c = 1
    i = 0
    while (i < len(a)):
        c = c * a[i] % n
        i += 1
    return c


# Miller Rabin primality test
# p is the number to check for primality, n is the strength of the test
# The chance a number passes this test but is not prime is 1/4^n
def primeToLimit(p, limit):
    if (p % 2 == 0):
        return False
    n = 3
    s = p / 2
    while (n < limit and n < s):
        if (p % n == 0):
            return False
        n = n + 2
    return True


def miller_rabin(p, n=10):
    # Base case: do a quick run through of the factors up to 65537 since this is a little faster in the low numbers
    # if not primeToLimit(p, 65537):  # 515507):
    #     return False
    # I cannot remember the specifics of the algorithm, but if you look up Miller-Rabin Primality test, it will give you
    # psuedo code which is implemented here in python.
    i = 0
    d = p - 1
    s = 0
    while (d % 2 == 0):
        d = d / 2
        s += 1
    # print(s, d)
    while (i < n):
        a = randint(2, p - 2)
        # print('a is', a)
        x = modpower(a, d, p)
        # print('x is', x)
        if (x == 1 or x == p - 1):
            i += 1
            continue
        # print('onward')
        k = 0
        while (k < s - 1):
            x = modpower(x, 2, p)
            if (x == 1):
                return False
            if (x == p - 1):
                break
            k += 1
        if (x == p - 1):
            i += 1
            continue
        return False
    return True
