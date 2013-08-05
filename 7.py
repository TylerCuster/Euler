def numPrime(n):
    primes = [2, 3]
    for c in range(5, n*11):
        tally = 0
        for d in range(2, c/2):
            if c%d != 0:
                tally += 1
        if tally == c/2-2:
            primes.append(c)
        if c%100 == 0:
            print c
    return primes[n-1]

# Slow as hell way to find 10001st prime -- by calculating 'em all

print numPrime(10001)
