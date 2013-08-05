def sumPrimes(limit):
    primes = [2, 3]
    for c in range(5, limit):
        tally = 0
        for d in range(2, c/2):
            if c%d != 0:
                tally += 1
        if tally == c/2-2:
            primes.append(c)
    
