# Consecutitve prime sum

def Sieve(n):
    primes = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    for p in range(n+1):
        if prime[p]:
            primes.append(p)
    return primes


def consecutivePrimes(primes):
    bigCounter = bigPrime = 0
    for i in range(len(primes)//4):
        total = counter = 0
        for j in range(i, len(primes)):
            total += primes[j]
            counter += 1
            if total in primes and counter > bigCounter:
                bigCounter = counter
                bigPrime = total
                print(bigPrime, bigCounter)
            if total > 1000000:
                total = 0
                counter = 0
                break
    return bigPrime, bigCounter

