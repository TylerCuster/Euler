import math
def largestPrimeFactor(limit, n):
    # Returns largest prime factor of n
    primes = [2, 3]
    for c in range(5, limit):
        tally = 0
        for d in range(2, c/2):
            if c%d != 0:
                tally += 1
        if tally == c/2-2:
            primes.append(c)
    count = 0
    while count < limit:
        count += 1
        if n%primes[-1] == 0:
            print primes[-1]
            return primes[-1]
        else:
            del primes[-1]

print largestPrimeFactor(100000, 600851475143)

def test():
    print largestPrimeFactor(100)
    print largestPrimeFactor(98)
    print largestPrimeFactor(38)
    print largestPrimeFactor(30)
    print largestPrimeFactor(15)

##test()
